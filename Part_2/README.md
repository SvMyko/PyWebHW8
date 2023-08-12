# Homework 8 Part 2  

## RabbitMQ Email Distribution Simulation

This project demonstrates the simulation of email distribution using RabbitMQ, along with MongoDB integration using the ODM Mongoengine.

## Prerequisites

1. Python 3.x
2. RabbitMQ server running locally or at a reachable address
3. MongoDB database
4. Required Python packages: `pika`, `mongoengine`, `faker` (install using `pip install pika mongoengine faker`)


## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.


## Project Structure

- `models.py`: Defines the MongoDB model for Contact with required fields such as full name, email, and is_message_sent.
- `connection.py`: Provides a function to connect to the MongoDB database.
- `producer.py`: Generates fake contact data, saves it to the database, and publishes messages to the RabbitMQ queue.
- `consumer.py`: Listens to the RabbitMQ queue, processes messages, simulates sending emails, and updates the is_message_sent field.

## Usage

1. Start RabbitMQ server and MongoDB database.

2. Update the connection details for MongoDB and RabbitMQ in `connection.py`.

3. Run `producer.py` to generate fake contact data, save it to the database, and publish messages to the RabbitMQ queue.

    ```
    python producer.py
    ```

4. Run `consumer.py` to listen to the RabbitMQ queue, process messages, simulate sending emails, and update the is_message_sent field.

    ```
    python consumer.py
    ```
## License
This project is licensed under the MIT License.