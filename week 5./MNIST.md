- **MNIST DataSet**
    - **손으로 작성된 DataSet,** 0-9까지 숫자 이미지로 구성이 되어있다.
        1. **Train Set** : 60000장의 image와 labels로 구성되어 있다.
        2. **Test Set** : 10000장의 image와 labels로 구성되어 있다.
    - 28 X 28 해상도의 image
        - 입력으로 들어가는 X의 갯수는 28 * 28 = 784개이고, 실제 Pythorch에서는 view라는 함수를 이용해 28 X 28 image를 784개로 변환해 사용하게 된다.
    - 1 channel gray image
    - 0-9 digits
    
- **torchvision**
    - Pythorch에서 사용하는 패키지 중 하나로 다양하게 사용되는 유명한 DataSet, Architectures, Transform들을 쉽게 읽어올 수 있다.

- **Reading Data**
    
    ```python
    import torchvision.datasets as dsets
    ...
    mnist_train = dsets.MNIST(root = "MNIST_data/", train = True, transform = transforms.ToTensor(), download = True)
    mnist_test = dsets.MNIST(root = "MNIST_data/", traing = False, transform = transforms.ToTensor(), download = True)
    
    data_loader = torch.utils.DataLoader(DataLoader = mnist_train, batch_size = batch_size, shuffle = True, drop_last = True)
    
    ...
    for epoch in range(training_epochs):
    ...
    	for X, Y in data_loader:
    		# reshape input image into [batch_size by 784]
    		# Label is not one-hot encoded
    		X  = X.view(-1, 28 * 28).to(device)
    ```
    
    - 일반적으로 Pythorch의 경우 0-1사이의 값을 가지고, 순서는 channel, height, weight이다.
    - 일반적인 image는 0-255사이의 값을 가지고, 순서는 channel, height, weight이다.
        - **image의 값과 순서를 Pythorch에 맞게 바꿔주는 작업을 ToTensor()가 진행한다.**
    - **epoch**
        - for문을 통해서 불러오고 X는 image, Y는 labels(0-9 사이 숫자 image)을 불러온다.
        - for문 안에서 view 이용해 28 * 28을 784로 바꿔주게 되고, X는 batch_size, 1 channel, 28 height, 28 weight에서 → batch_size, 784로 변환된다.
        - **epoch**
            - **traning set 전체가 한번 학습에 사용**되면 **1 epoch**이 돌았다. 라고 표현한다.
            - 즉 **60000장 전체가 사용 되면 1 epoch**이다.
        - **batch_size**
            - 가능하면 60000장을 한번에 학습하는 것이 좋다. 하지만 메모리와 속도를 고려해 **분리해서 사용**을 하게 된다.
            - 이때 **분리하는 크기를 batch size**라고 한다.
        - **iteration**
            - batch를 몇 번 학습에 사용했는가를 나타낸다.
            - **1000개의 traning set이 있을 때 bacth size는 500으로 정했다. 따라서 2개의 batch가 있다는 것이므로 iteration은 2이다. 
            2 iteration을 사용하게 되면 1 epoch이 완료된다.**
            
- **Softmax (학습 과정)**
    
    ```python
    # MNIST data image of shape 28 * 28 = 784
    linear = torch.nn.Linear(784, 10, bias = True).to(device)
    
    # parameters
    training_epochs = 15
    batch_size = 100
    
    # define cost / Loss & optimizer
    criterion = torch.nn.CrossEntropyLoss().to(device) # Softmax is internally computed
    optimizer = torch.optim.SGD(linear.parameters(), lr = 0.1)
    
    for epoch in range(training_epochs):
      avg_cost = 0
      total_batch = data_loader 
    
      for X, Y in data_loader: 
    		# reshape input image into [batch_size by 784]
    		# Label is not one-hot encoded
    		# 아래 과정을 batch_size가 전체 train dataset, 즉 1 epoch이 돌 때까지 계속해서 반복하게 된다. 
        X = X.view(-1, 28 * 28).to(device)
        optimizer.zero_grad()
        hypothesis = linear(X)
        cost = criterion(hypothesis, Y)
        cost.backward()
        optimizer.step()
        avg_cost += cost / total_batch
    
      print("Epoch: ", "%04d" % (epoch + 1), "cost =", "{:.9f}".format(avg_cost))
    ```

- **Test (학습 후 테스트 과정)**
    
    ```python
    # Test the model using test sets
    With torch.no_grad(): # grad 계산을 하지 않겠다는 의미이다. 
    	X_test = mnist_test.test_data.view(-1, 28 * 28).float().to(device)
    	Y_test = mnist_test.test_labels.to(device)
    	
    	prediction = linear(X_test)
    	correct_prediction = torch.argmax(prediction, 1) == Y_test
    	accuracy = correct_prediction.float().mean()
    	print("Accuracy: ", accuracy.item())
    ```
    
- **Visualization (테스트 이미지를 시각화)**
    
    ```python
    import matplotlib pyplot as plt
    import random
    ...
    r = random.randint(0, len(mnist_test) - 1)
    X_single_data = mnist_test.test_data[r:r + 1].view(-1, 28 * 28).float().to(device)
    Y_single_data = mnist_test.test_labels[r: + r + 1].to(device)
    
    print("Lable: ", Y_single_data.item())
    single_prediction = linear(X_single_data)
    print("Prediction: ", torch.argmax(single_prediction, 1).item())
    
    plt.imshow(mnist_test.test_data[r:r + 1].view(28, 28), cmap = "Greys", interpolation = "nearest")
    plt.show()
    ```