def main(args):
    # load data
    train_loader = torch.utils.data.DataLoader(datasets.MNIST(...), batch_size=args['batch_size'], shuffle=True)
    test_loader = torch.tuils.data.DataLoader(datasets.MNIST(...), batch_size=1000, shuffle=True)
    # build model
    model = Net(hidden_size=args['hidden_size'])
    optimizer = optim.SGD(model.parameters(), lr=args['lr'], momentum=args['momentum'])
    # train
    for epoch in range(10):
        train(args, model, device, train_loader, optimizer, epoch)
        test_acc = test(args, model, device, test_loader)
        print(test_acc)
    print('final accuracy:', test_acc)

if __name__ == '__main__':
    params = {
        'batch_size': 32,
        'hidden_size': 128,
        'lr': 0.001,
        'momentum': 0.5
    }
    main(params)