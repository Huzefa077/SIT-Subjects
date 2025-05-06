#include<vector>
#include<climits>
#include<iostream>
#include<omp.h>
using namespace std;

void reduction_min(vector<int>& arr){
    int min_value = INT_MAX;
    #pragma omp parallel for reduction(min:min_value)
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] < min_value){
            min_value = arr[i];
        }
    }
    cout << "MINIMUM VALUE : " << min_value << endl;
}
void reduction_max(vector<int>& arr){
    int max_value = INT_MIN;
    #pragma omp parallel for reduction(max:max_value)
    for(int i=0 ; i<arr.size() ; i++){
        if(arr[i]>max_value){
            max_value = arr[i];
        }
    }
    cout<<"MAXIMUM VALUE : " <<max_value << endl;
}
void reduction_sum(vector<int>& arr){
    int sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for (int i=0 ; i<arr.size() ; i++){
        sum+=arr[i];
    }
    cout<<"SUM = "<<sum<<endl;
}
void reduction_average(vector<int>& arr){
    int sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for (int i=0 ; i<arr.size() ; i++){
        sum+=arr[i];
    }
    cout<<"AVERAGE = "<<(double)sum / arr.size()<<endl;

}

int main(){
    vector<int> arr = {4,2,6,5,87,12,11,9};
    reduction_min(arr);
    reduction_max(arr);
    reduction_sum(arr);
    reduction_average(arr);
}