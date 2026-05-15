class DynamicArray {
private:
    int* dynarr;
    int dyncapacity;
    int length;

public:
    DynamicArray(int capacity) {
        dyncapacity = capacity;
        length = 0;
        dynarr = new int[capacity];
    }

    int get(int i) {
        return this->dynarr[i]; 
    }

    void set(int i, int n) {
        this->dynarr[i] = n;
    }

    void pushback(int n) {
        if (this->length == this->dyncapacity) { 
            resize();
        }
        this->dynarr[this->length] = n; 
        this->length++; 
    }

    int popback() {
        int tmp = dynarr[this->length - 1];
        length--; 
        return tmp;
    }

    void resize() {
        int new_capacity = 2 * this->dyncapacity; 
        int* newarr = new int[new_capacity]; 
        for (int i = 0; i < this->length; i++) { 
            newarr[i] = this->dynarr[i]; 
        }
        delete[] this->dynarr;
        this->dynarr = newarr; 
        this->dyncapacity = new_capacity; 
    }
 
    int getSize() {
        return this->length;
    }

    int getCapacity() {
        return this->dyncapacity;
    }
};
