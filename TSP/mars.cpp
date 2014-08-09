#include <iostream>
#include <vector>
#include <climits> //For INT_MAX
#include <math.h>
#include <stack>
#include <algorithm>
#include "mars.h"

using namespace std;
int size;
std::vector<POINT> points;
std::vector<int> result;
double curBest;
std::vector<std::vector<int> > minimalTwo;
void twoOPT(std::vector<int> &Route, int start, int end, int &best);
double Greedy(vector<POINT> &points){
	
	bool visted[size];
	vector<int> Route;
	Route.resize(size);
	for(int i=0;i<size;i++)
		visted[i]=false;
	visted[0]=true;
	int RouteIndex=0;
	double TotalWeight=0;
	for(int i=0;;){
		
		double minDistance= INT_MAX;
		int minIndex=-1;
		
		for(int j=0;j<size;j++){
			
			if((!visted[j])&&mdistance(points[i],points[j])<minDistance){
				
				minDistance = mdistance(points[i],points[j]);
				minIndex=j;	
			}
		}
		
		if(minIndex==-1){
			Route[size-1]=0;
			TotalWeight+=mdistance(points[i],points[0]);
			break;
		}
		Route[RouteIndex++]=minIndex;

		i=minIndex;
		visted[i]=true;
		TotalWeight+=minDistance;
		


	}
	
	int best=TotalWeight;
	cout << TotalWeight << endl;
	// if(size>=20){
	// 	reverse(Route.begin(),Route.end());
		
	// 	for(int k=0;k<20;k++){
				
	// 		for(int i=0;i<size;i++){
	// 			for(int j=0;j<size;j++)
	// 				twoOPT(Route,j,i,best);
				
	// 		}
			
	// 		//reverse(Route.begin(),Route.end());
			
			
	// 	}
	// 	reverse(Route.begin()+1,Route.end());
	// 	for(int k=0;k<20;k++){
			
	// 		for(int i=0;i<size;i++){
	// 			for(int j=0;j<size;j++)
	// 				twoOPT(Route,j,i,best);
				
	// 		}
			
	// 		//reverse(Route.begin(),Route.end());
			
			
	// 	}
	// }
	// else{
	// 	reverse(Route.begin(),Route.end());
		
	// 	for(int k=0;k<2;k++){
				
	// 		for(int i=0;i<size;i++){
	// 			for(int j=0;j<size;j++)
	// 				twoOPT(Route,j,i,best);
				
	// 		}
			
	// 		//reverse(Route.begin(),Route.end());
			
			
	// 	}
	// 	reverse(Route.begin()+1,Route.end());
	// 	for(int k=0;k<2;k++){
			
	// 		for(int i=0;i<size;i++){
	// 			for(int j=0;j<size;j++)
	// 				twoOPT(Route,j,i,best);
				
	// 		}
			
	// 		//reverse(Route.begin(),Route.end());
			
			
	// 	}
	// }
	

	return best;

}
double MSTWeight(vector<POINT> &points){
	int size=points.size();
	bool inMST[size];
	
	double dist[size];
	for(int i=0;i<size;i++){
		dist[i]=INT_MAX;
		inMST[i]=false;
	}
	dist[0]=0;
	for(int i=0;i<size-1;i++){	
		int index=minDistPoint(inMST,dist,size); //O(V)
		inMST[index]=true;
		for(int j=0;j<size;j++){
			if((!inMST[j])&&mdistance(points[j],points[index])<dist[j]){
				
				dist[j]=mdistance(points[j],points[index]);

			}
		}
	}
	double TotalWeight=0;
	for(int i=0;i<size;i++){
		TotalWeight+=dist[i];
	}
	return TotalWeight;
}



void Search(int tourlength, double tourWeight, 
	bool visted[], int curPointIndex, int next[]){
	//cout<<"Search"<<endl;
	//cout<<curBest<<endl;
	if(tourlength==size){
		//record
		if(tourWeight+mdistance(points[curPointIndex],points[0])<=curBest){
			curBest=tourWeight+mdistance(points[curPointIndex],points[0]);
			cout<<"curBest "<<curBest<<endl;
			for(int i=0;i<size;i++){
				result[i]=next[i];

			}
			result[curPointIndex]=0;
			
		}
		return;
	}
	else{
		
		int count=0;
		for(int i=0;i<size;i++){
			if(!visted[i]){
				++count;
			}
		}
		if(count>=5||(size>=20 && count>=2)){
			double curLowerBound=0;
			
			for(int i=0;i<size;i++){
				if(!visted[i]){
					curLowerBound+=(minimalTwo[i][0]+minimalTwo[i][1])/2;
				}
			}
			
			curLowerBound+=(minimalTwo[curPointIndex][0]+minimalTwo[0][0])/2;
			
			if(curLowerBound+tourWeight>curBest){
				// cout<<"Linear"<<curLowerBound<<endl;
				return;
			}
		}
		if(count>=5){
			
			//Lower Bound need to renew by the shortest connection between two unconnected graph
			//we need TourWeigh+ MSTWeight+2d> curBest now O(n^2) not working well
			
			double Distance = minimalTwo[curPointIndex][0]+minimalTwo[0][0];

		



			std::vector<POINT> temp;
			for(int i=0;i<size;i++){
				if(!visted[i]){
					temp.push_back(points[i]);
				}
			}

			int MSTWeightVal=MSTWeight(temp);
			if(MSTWeightVal+tourWeight+Distance>curBest){
				// cout<<"MST"<<MSTWeightVal<<endl;
				return;
			}
		}
		

		for(int i=0;i<size;i++){
			
			if(!visted[i]){
				
				if(tourWeight+mdistance(points[i],points[curPointIndex]) < curBest){
					visted[i]=true;
					next[curPointIndex]=i;
					Search(tourlength+1,tourWeight+mdistance(points[i],points[curPointIndex]),visted
						,i, next);
					
					
					visted[i]=false;
				}
			}	
		}
	}
}


void OPTTSP(vector<POINT> &points){
	
	
	bool visted[size]; 
	
	
	for(int i=0;i<size;i++)
		visted[i]=false;
	visted[0]=true;
	int next[size];

	curBest=Greedy(points); //Greedy Best O(n^2)
	
	//Need to have the minimal two edges for each vertex
	minimalTwo.resize(size);
	for(int i=0;i<size;i++){
		minimalTwo[i].resize(2);
		minimalTwo[i][0]=INT_MAX;
		minimalTwo[i][1]=INT_MAX;
	}
	for (int i = 0; i < size; ++i)
	{
		for(int j=0;j<size;++j){
			if(j!=i){
				if(mdistance(points[i],points[j])<minimalTwo[i][0]){
					minimalTwo[i][1]=minimalTwo[i][0];
					minimalTwo[i][0]=mdistance(points[i],points[j]);
		
				}
				else{
		
					if(mdistance(points[i],points[j])<minimalTwo[i][1]){
						minimalTwo[i][1]=mdistance(points[i],points[j]);
					}
				}
			}
		}
	}
	
	
	result.resize(size);
	Search(1,0,visted,0,next);
	cout<<curBest<<endl;
	
	
}



void twoOPT(std::vector<int> &Route, int start, int end, int &best){
	if(end<=start||end>=size-1)
		return;
	double diff=mdistance(points[Route[start]],points[Route[start+1]])+
		mdistance(points[Route[end]],points[Route[end+1]])-
		mdistance(points[Route[start+1]],points[Route[end+1]])-
		mdistance(points[Route[end]],points[Route[start]]);
	if(diff<=0)
		return;
	else{
		// cout<<"diff "<<diff<<endl;
		// cout<<"se "<<start<<" "<<end<<endl;
		for(int i=0;i<(end-start)/2;i++){
			swap(Route[start+1+i],Route[end-i]);
			//cout<<"swap"<<endl;
		}
		// cout<<"Route ";
		// for(int i=0;i<size;i++){
		// 	cout<<Route[i]<<" ";
		// }
		// cout<<"\n";
		best-=diff;
		
	}
}




int main(int argc, char** argv){
	string mode;
	// vector<POINT> points;
	
	init(points);
	size = points.size();
	cout << size <<endl;
    points[0].toString();
	
	
	OPTTSP(points);
	

}


