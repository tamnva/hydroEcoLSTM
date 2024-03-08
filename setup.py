from setuptools import setup

setup(
    name='hydroecolstm',
    version='0.1.0',    
    description='A python package for HydroEcological Modelling using LSTM',
    url='https://github.com/tamnva/HydroPyTorch',
    download_url = "https://github.com/tamnva/hydroecolstm/archive/refs/tags/v0.2.0.tar.gz",
    author='Tam V. Nguyen',
    author_email='tamnva@gmail.com',
    license='GPLv3',
    packages=['hydroecolstm', 
              'hydroecolstm.data',
              'hydroecolstm.interface', 
              'hydroecolstm.utility', 
              'hydroecolstm.model',
              'hydroecolstm.train'],
    python_requires='>=3.8',
    install_requires=['pandas>=2.2.0',
                      'numpy>=1.24.4',
                      'torch>=2.1.0',
                      'pandastable>=0.13.1',
                      'tkcalendar>=1.6.1',
                      'PyYAML>=6.0.1',
                      'pathlib>=1.0.1',
                      'customtkinter>=5.2.1',
                      'CTkToolTip>=0.8',
                      'CTkMessagebox>=2.5',
                      'CTkListbox>=0.10'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPL-3.0 license ',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)
