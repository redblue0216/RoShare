from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'roshareclient',
        version = '0.1.1',
        author = 'shihua',
        author_email = "15021408795@163.com",
        python_requires = ">=3.9.13",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = 'RoShareClient is a python sdk with chinese stock data client',
        # install_requires = ['click','fastapi','rich','pyjwt'],

        # ### 包接入点，命令行索引
        # entry_points = {
        #     'console_scripts': [
        #         'roshareservicectl = roshareservice.cli:roshareservice'
        #     ]
        # }      
)