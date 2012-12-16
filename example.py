if __name__ == "__main__":
    import sys
    sys.path.append('../jars/esper-4.7.0.jar')
    sys.path.append('../jars/cglib-nodep-2.2.jar')
    sys.path.append('../jars/commons-logging-1.1.1.jar')
    sys.path.append('../jars/antlr-runtime-3.2.jar')
    
    #sys.path.append('../../py/bogusd')
    
    import random
    import java.util.Map as Map
    import java.lang.Double 
    from jython_utils import jfloat
    from jycep import EsperEngine
    from jycep import EsperStatement
    from jycep import EventListener
    #import bogusd

    cep = EsperEngine("TestEngine")
    
    cep.define_event("BogusEvent", {"P1": jfloat, 
                                    "P2": jfloat,
                                    "P3": jfloat, 
                                    "P4": jfloat})

    cep.start()

    #datagen = bogusd.Generator()
    #datagen.append(bogusd.Point('P1'))
    #datagen.append(bogusd.Point('P2'))
    #datagen.append(bogusd.Point('P3'))
    #datagen.append(bogusd.Point('P4'))

    def callback(data_new, data_old):
        print("New Data:" + str(data_new))
        print("Old Data:" + str(data_old))

    def endcallback():
        print('Input terminated')

    stmt = cep.create_query('select * from BogusEvent(P2 > 2.0).win:length(3)')
    stmt.addListener(EventListener(callback))      
     
    cep.send_event({"P1": 1.1, "P2": 1.2, "P3": 1.3, "P4": 1.4},
                   "BogusEvent")
    cep.send_event({"P1": 2.1, "P2": 2.2, "P3": 2.3, "P4": 2.4},
                   "BogusEvent")
    cep.send_event({"P1": 3.1, "P2": 3.2, "P3": 3.3, "P4": 3.4},
                   "BogusEvent")                   
    cep.send_event({"P1": 4.1, "P2": 4.2, "P3": 4.3, "P4": 4.4},
                   "BogusEvent")                   
    cep.send_event({"P1": 5.1, "P2": 5.2, "P3": 5.3, "P4": 5.4},
                   "BogusEvent")
    cep.send_event({"P1": 6.1, "P2": 6.2, "P3": 6.3, "P4": 6.4},
                   "BogusEvent")
    cep.send_event({"P1": 7.1, "P2": 7.2, "P3": 7.3, "P4": 7.4},
                   "BogusEvent")                   
    cep.send_event({"P1": 8.1, "P2": 8.2, "P3": 8.3, "P4": 8.4},
                   "BogusEvent") 
                   
    #streamer = bogusd.FixedIntervalScheduler(callback, datagen, 0.1,
    #                                         endcallback, 10)
    #streamer.start()
