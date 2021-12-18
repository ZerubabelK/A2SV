void countSwaps(vector<int> a) {
    int count=0;
    for(int i=0;i<a.size();i++){
        for(int j=0;j<a.size()-1;j++){
            if(a.at(j)>a.at(j+1)){
                int temp = a.at(j);
                a.at(j)=a.at(j+1);
                a.at(j+1)=temp;
                count++;
            }
        }
    }
    cout<<"Array is sorted in "<< count <<" swaps."<<endl;
    cout<<"First Element: "<<a.at(0)<<endl;
    cout<<"Last Element: "<<a.at(a.size()-1)<<endl;
}