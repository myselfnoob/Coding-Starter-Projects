//Implementation of Circular Queue

#include<iostream>
using namespace std;

class Queue{
    private:
    int queue[7];
    int rear=-1;
    int front=0;
    int size=0;
    public:

    bool isempty(){
        if (size==0) return true;
        else return false;
    }
    bool isfull(){
        if (size==7) return true;
        else return false;
    }
    void enqueue(int x){
        if(!isfull()){
            rear=(rear+1)%7;
            queue[rear]=x;
            size++;
        }
        else{
            cout<<"Overflow"<<endl;
        }}
    void dequeue(){
        if(!isempty()){
            front=(front+1)%7;
            size--;
        }
        else{
            cout<<"Underflow"<<endl;
        }
    }
    friend void display(Queue Q);
};

void display(Queue Q){
    for(int i=Q.front;i<=Q.rear;i++){
        cout<<Q.queue[i]<<" ";
    }
    cout<<"\n";
}

int main(){
    Queue q1;
    while(1){
        cout<<"Enter 1 for Enqueue"<<endl;
        cout<<"Enter 2 for Dequeue"<<endl;
        cout<<"Enter 3 for Display"<<endl;
        cout<<"Enter 4 for Exit"<<endl;
        int chc,n;
        cin>>chc;
        switch(chc){
            case 1:
                cin>>n;
                q1.enqueue(n);
                break;
            case 2:
                q1.dequeue();
                break;
            case 3:
                display(q1);
                break;
            case 4:
                 return 0;

        }
    }
    return 0;
}