struct Node { 
    int val; 
    Node* next; 
};

class LinkedList {
private: 
    Node* head; 
    Node* tail; 
    int length;

public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
        length = 0;
    }

    int get(int index) {
        if (index < 0 || index >= this->length) { 
            return -1; 
        }
        Node* tmp = head;
        for (int i = 0; i < index; i++) { 
            tmp = tmp->next; 
        }
        return tmp->val;
    }   

    void insertHead(int val) {
        Node* new_node = new Node{val, nullptr};
        if (this->length == 0) { 
            head = new_node;
            tail = head;
        } else {
            new_node->next = head; 
            this->head = new_node;
        }
        this->length++; 
    }
    
    void insertTail(int val) {
        Node* new_node = new Node{val, nullptr};
        if (this->length == 0) { 
            this->head = new_node; 
            this->tail = this->head;
        } else { 
            tail->next = new_node; 
            this->tail = new_node;
        }
        this->length++;
    }

    bool remove(int index) {
        if (index < 0 || index >= length) return false;
        
        if (index == 0) {
            Node* temp = head;
            head = head->next;
            if (length == 1) tail = nullptr;
            delete temp;
        } else {
            Node* prev = head;
            for (int i = 0; i < index - 1; i++) prev = prev->next;
            Node* toDelete = prev->next;
            prev->next = toDelete->next;
            if (index == length - 1) tail = prev;
            delete toDelete;
        }
        length--;
        return true;
    }

    vector<int> getValues() {
        vector<int> values;
        Node* tmp = this->head; 
        while (tmp != nullptr) {
            values.push_back(tmp->val);
            tmp = tmp->next;
        }
        return values;
    }
};
