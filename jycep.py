import sys
import random
import java.util.Map as Map
import java.lang.Double
import jython_utils
from com.espertech.esper.client import EPServiceProviderManager
from com.espertech.esper.client import Configuration
from com.espertech.esper.client import EPServiceProvider
from com.espertech.esper.client import UpdateListener
from com.espertech.esper.client import EPStatement
from com.espertech.esper.client.soda import StreamSelector

ISTREAM_ONLY = StreamSelector.ISTREAM_ONLY 
RSTREAM_ONLY = StreamSelector.RSTREAM_ONLY
RSTREAM_ISTREAM_BOTH = StreamSelector.RSTREAM_ISTREAM_BOTH    
    
class _EventListener(UpdateListener):
    
    def __init__(self, handler):
        self.callback = handler
        
    
    def update(self, *args):
        """
        EventBean[] newEvents, EventBean[] oldEvents
        """
        #print('Got event:')
        #print(args)
        
        new_events = dict(args[0][0].getUnderlying())
        old_events = None
        if not args[1] is None:
            old_events = dict(args[1][0].getUnderlying())    
        
        self.callback(new_events, old_events)

        
def EventListener(fnctn):
    return _EventListener(fnctn)
        

class EsperStatement(EPStatement):
    """
    com.espertech.esper.client.EPStatement :
        http://esper.codehaus.org/esper-4.7.0/
        doc/api/com/espertech/esper/client/EPStatement.html
    """
    pass    
    
class EsperEngine():

    def __init__(self, engine_id):
        self.engine_id = engine_id
        self._cnfg = Configuration()
        self._esperService = None

    def define_event(self, eventtype, eventspec):
        self._cnfg.addEventType(eventtype, eventspec)

    def send_event(self, event, eventtype):
        self._esperService.getEPRuntime().sendEvent(event, eventtype)

    def start(self):
        self._cnfg.getEngineDefaults().getStreamSelection().\
            setDefaultStreamSelector(RSTREAM_ISTREAM_BOTH)    
        self._esperService = EPServiceProviderManager.\
            getProvider(self.engine_id, self._cnfg)
        self._esperService.initialize()

    def create_query(self, stmt):
        return self._esperService.getEPAdministrator().createEPL(stmt)