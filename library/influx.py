
import json
import datetime
import logging

from influxdb import InfluxDBClient


class influxWrapper(object):

    def __init__(self,  logger):
        """Instantiate a connection to the InfluxDB."""
    #    self._host = host
     #   self._port = port

      #  self._dbuser = dbuser
      #  self._dbpasswd = dbpasswd
        self._dbname = ''

        _libName = str(__name__.rsplit('.',1)[-1])
        self._log = logging.getLogger(logger + '.'+ _libName + '.' + self.__class__.__name__)

        self._log.debug('Create Instance of Class: influx wrapper')

       # self._client = InfluxDBClient(host, port, dbuser, dbpasswd, dbname)

        self._measure = {}
        self._measures = []

    def connectDB(self,host='localhost', port=8086, dbuser='root', dbpasswd='password', dbname='measurement'):
        self._log.debug("Connect to influxDB: " + self._dbname)
        self._dbname = dbname
        self._client = InfluxDBClient(host, port, dbuser, dbpasswd, dbname)
        return True


    def createDB(self):

        self._log.debug("Create database: " + self._dbname)
        self._client.create_database(self._dbname)
        return True

    def retentionPolicy(self,name,policy):

        self._log.debug("Create a retention policy")
        self._client.create_retention_policy(name, policy, 3, default=True)
        return True

    def writePoints(self, jsonBody):
        self._log.debug("Write points: {0}".format(jsonBody))
        if self._client.write_points(jsonBody, time_precision='ms'):
            self._log.info("Wrote data points to DB: %s", jsonBody)
            return True
        else:
            self._log.erro("Failed to write data points to DB %s",jsonBody)
        return False

    def setDBName(self,dbname):
        self._dbname = dbname
        return True

    def addTag(self,tag,value):
        self._measure[tag]=value

    def createHaeder(self,tags):
        self._log.debug('Methode: createHeader with tags: %s',tags)

        self._measure['measurement']= self._dbname
        self._measure['tags']= tags

    #    print(self._measure)
        self._log.debug('Header created %s',self._measure)
        return True

    def storeMeasurement(self,fields):
        self._measure['time'] = datetime.datetime.utcnow().isoformat()
        self._measure['fields'] = fields
        self._measures.append(self._measure)
        return self._measure

    def writeMeasures(self):
        self._log.debug('Methode: writeMeasures')
        if self.writePoints(self._measures):
            self._log.debug('wrote Points %d with success', len(self._measures))
        #else:
       #     self._log.error('failed to write datapoints to DB: %s',self._measure)
       # print(self._measures)
        return True


if __name__ == '__main__':
    influx = influxWrapper('xx')
    influx.connectDB('192.168.20.205',8086,'testuser','test123','testmeasure')
    influx.createDB()
  #  influx.writePoints()

    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    influx.writePoints(json_body)
    influx.createHaeder({'TEST1': 'TESST1','TEST2':'TEST2'})
    influx.storeMeasurement({'MEASURE1':'123', 'MEASURE2':'0.65673','MEASURE3': 'TESTERESF'})
    influx.storeMeasurement({'MEASURE1': '123', 'MEASURE2': '0.65673', 'MEASURE3': 'TESTERESF'})
    influx.storeMeasurement({'MEASURE1': '123', 'MEASURE2': '0.65673', 'MEASURE3': 'TESTERESF'})
    influx.writeMeasures()