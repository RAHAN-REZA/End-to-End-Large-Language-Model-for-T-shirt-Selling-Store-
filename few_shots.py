few_shots =[
           {'Question': "How many t-shirt do we have left for nike in extra small size and blue color?",
            "SQLQuery": "SELECT stock_quantity FROM t_shirts WHERE brand = 'Nike' AND color = 'Blue' AND size = 'XS'",
            "SQLResult": "Result of the SQL query",
            "Answer": '98'},
           {'Question':"How much is the price of the inventory for all small size t-shirts?",
           "SQLQuery":"select sum(price*stock_quantity) from t_shirts where size=S",
            "SQLResult": "Result of the SQL query",
           "Answer": '382'},
           {'Question':"if we have to sell all the levi's t-shirts today with discounts applied.How much revenue our store will generate(post discounts)?",
           "SQLQuery":"""select sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from 
                      (select sum(price*stock_quantity) as total_amount,t_shirt_id from t_shirts where brand = 'Levi'
                       group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id""",
           "SQLResult": "Result of the SQL query",
           "Answer": '28931.4'},
           {'Question':"If we have to sell  all the levi's t-shirt today.How much revenue will we generate?",
           "SQLQuery":"select sum(price*stock_quantity)from t_shirts where brand='Levi'",
           "SQLResult": "Result of the SQL query",
             "Answer":'31194'},
            {'Question':"How much white color levi's t-shirts we have available?",
            "SQLQuery":"select sum(stock_quantity) from t_shirts where brand= levi and color = white",
            "SQLResult": "Result of the SQL query",
            "Answer": '58'},
            {'Question':"how much is the price of all extra small size t-shirts?",
             "SQLQuery":"select sum(price*stock_quantity) from t_shirts where size='XS'",
            "SQLResult":"Result of the SQL query",
             "Answer":'286'}
]