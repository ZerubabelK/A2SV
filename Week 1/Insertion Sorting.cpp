void insertionSort1(int n, vector<int> arr) {
    bool c=true;
    int temp = arr.at(arr.size()-1);
    for(int i=arr.size()-1;i>=0;i--){
        if(i!=0 && temp<arr.at(i-1)){
            arr.at(i)=arr.at(i-1);
        }
        else if(i!=0 && temp>arr.at(i-1)){
            arr.at(i)=temp;
            c=false;
        }
        else if(i==0 && temp<arr.at(i)){
            arr.at(0)=temp;
        }
        for(int j=0;j<arr.size();j++){
            cout<<arr.at(j)<<" ";
        }
        cout<<endl;
        if(c==false){
            break;
        }
    }
}