'''
Function to create personalize metrics box
'''
def metrics(sline, i):
    fontsize = 14
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

    htmlstr = f"""<p style='background-color: "#D4C19C";
                            color:"#D4C19C";
                            font-size: {fontsize}px;
                            border-width: 1px;
                            border-style: solid;
                            border-radius: 7px;
                            text-align: center;
                            line-height: 30px;'>
                            <span style='font-size: 20px;
                            font-weight: bold;
                            margin: 0px;
                            padding: 0px;
                            text-align: center;'>{sline}</style></span>
                            <br>
                            <i class= fa-xs'></i> {i}
                            </style>
                            </p>
                            """
    
    return lnk + htmlstr