//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QNmeaSatelliteReader that Python can take functions over in. Every QNmeaSatelliteReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaSatelliteReaderCall0)(const void *, int *);
class CuteQNmeaSatelliteReader : public QNmeaSatelliteReader {
public:
  using QNmeaSatelliteReader::QNmeaSatelliteReader;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QNmeaSatelliteReader17readAvailableDataEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QNmeaSatelliteReader::readAvailableData()
  void readAvailableData() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaSatelliteReaderCall0 call = reinterpret_cast<CuteQNmeaSatelliteReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QNmeaSatelliteReader::~QNmeaSatelliteReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNmeaSatelliteReaderD1Ev(QNmeaSatelliteReader *self) {
  delete self;
}

//  void QNmeaSatelliteReader::readAvailableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNmeaSatelliteReader17readAvailableDataEv(
    QNmeaSatelliteReader *self) {
  self->readAvailableData();
}

//  a Python function taken by a CuteQNmeaSatelliteReader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaSatelliteReader(
    QNmeaSatelliteReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaSatelliteReader *>(self)->take(key, call);
}
