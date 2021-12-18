vector<int> gradingStudents(vector<int> grades) {
    for(int i=0;i<grades.size();i++){
    
        if(grades.at(i)<38){
            continue;
        }
        else if(grades.at(i)>=38){
            for(int j=grades.at(i);j<=grades.at(i)+2;j++){
                if(j%5==0){
                    grades.at(i)=j;
                }
            }
        }
    }
    return grades;
}