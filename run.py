from apiflask_first import create_app


if __name__ == '__main__':
    APP = create_app()
    APP.run(host="0.0.0.0", port=5000)