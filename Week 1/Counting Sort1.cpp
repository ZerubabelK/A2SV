vector<int> countingSort(vector<int> arr) {
    vector<int> counters(100);
    for(int i=0;i<arr.size();i++){
        counters.at(arr.at(i))++;
    }
    return counters;
}