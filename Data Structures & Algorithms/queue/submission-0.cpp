#include <iostream>
#include <stdexcept> // For handling empty pop errors

struct Node { 
    int data; 
    Node* next;
    Node* prev;  

    // Added a constructor for clean node instantiation
    Node(int val, Node* nxt = nullptr, Node* prv = nullptr) 
        : data(val), next(nxt), prev(prv) {}
};

class Deque {
private:
    // Define class members here so they persist across method calls
    Node* head; 
    Node* tail; 
    int length; 

public:
    // Properly initialize members using an initialization list
    Deque() : head(nullptr), tail(nullptr), length(0) {}

    // Destructor to prevent memory leaks when the Deque goes out of scope
    ~Deque() {
        while (!isEmpty()) {
            popleft();
        }
    }

    bool isEmpty() {
        return this->length == 0; 
    }

    int getLength() {
        return this->length;
    }

    void append(int value) {
        if (this->tail == nullptr) { 
            // Correct allocation using 'new'
            this->head = new Node(value, nullptr, nullptr); 
            this->tail = this->head; 
        } else {
            this->tail->next = new Node(value, nullptr, this->tail); 
            this->tail = this->tail->next; 
        }
        this->length++;
    }

    void appendleft(int value) {
        if (this->head == nullptr) { 
            this->head = new Node(value, nullptr, nullptr); 
            this->tail = this->head; 
        } else { 
            Node* new_head = new Node(value, this->head, nullptr); 
            this->head->prev = new_head; 
            this->head = new_head; 
        }
        this->length++;
    }

    int pop() {
        if (isEmpty()) {
            return -1;
        }

        int value = this->tail->data; // Save data to return it later
        Node* tmp = this->tail;

        if (this->length > 1) { 
            this->tail = this->tail->prev;
            this->tail->next = nullptr; // Clear out the old tail reference
        } else { 
            this->head = nullptr; 
            this->tail = nullptr; 
        }

        delete tmp; // Safely delete the old node
        this->length--;
        return value;
    }

    int popleft() {
        if (isEmpty()) {
             return -1;
        }

        int value = this->head->data; // Save data to return it later
        Node* tmp = this->head;

        if (this->length > 1) { 
            this->head = this->head->next; 
            this->head->prev = nullptr; // Clear out the old head reference
        } else { 
            this->head = nullptr; 
            this->tail = nullptr; 
        }

        delete tmp; // Safely delete the old node
        this->length--;
        return value;
    }
};