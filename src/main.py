import data_loader
import model
import strategy
import trader

def main():
    # Шаг 1: Получаем данные
    data = data_loader.get_historical_data()
    
    # Шаг 2: Подготовка данных
    sequences, labels = model.create_sequences(data['close'].values)
    
    # Шаг 3: Обучение модели
    lstm_model = model.build_model((sequences.shape[1], 1))
    lstm_model.fit(sequences, labels, epochs=5)
    
    # Шаг 4: Прогнозирование и торговая стратегия
    predictions = lstm_model.predict(sequences)
    action = strategy.trading_strategy(predictions)
    
    # Шаг 5: Выполнение торговой операции
    if action == "buy":
        trader.place_order(side="Buy")
    elif action == "sell":
        trader.place_order(side="Sell")

if __name__ == "__main__":
    main()
