from modeling import create_model
import data
from prediction import prediction

x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_test_scaled, x_test_1_scaled, y_test_scaled = data.preprocessing_data()
sequence_x = 180 * 4
sequence_y = 7
model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)

next_week_sales = prediction(x_test_scaled, x_test_1_scaled,
                             y_scaler, weight='1_bac2.hdf5', model=model)

print(next_week_sales)
