#ifndef MARS_H
#define MARS_H
#include <stdio.h>
using namespace std;
class POINT
{
	/* data */
public:
	double x;
	double y;

public:
	void toString(){
		cout<<"x: "<<x<<" y:" <<y<<endl;
	}
};


void init(vector<POINT> &points){
	int lines;
	cin>>lines;
	points.resize(lines);
	for(int i=0;i<lines;++i){
		float x,y;
		cin>>x;
		cin>>y;
		
		POINT temp;
		temp.x=x;
		temp.y=y;
		
		points[i]=temp;
		points[i].toString();
	}
}


int minDistPoint(bool inMST[], double dist[], int size){
	int min=INT_MAX;
	int min_index;
	for(int i=0;i<size;i++){
		if(inMST[i]==false && dist[i] < min){
			min=dist[i];
			min_index=i;
		}
	}
	return min_index;
}

double mdistance(POINT &A,POINT &B){
	return sqrt((A.x-B.x)*(A.x-B.x) + (A.y-B.y)*(A.y-B.y));
}







#endif