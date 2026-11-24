//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QNmeaReader that Python can take functions over in. Every QNmeaReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaReaderCall0)(const void *, int *);
class CuteQNmeaReader : public QNmeaReader {
public:
  using QNmeaReader::QNmeaReader;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QNmeaReader17readAvailableDataEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QNmeaReader::readAvailableData()
  void readAvailableData() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaReaderCall0 call = reinterpret_cast<CuteQNmeaReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QNmeaReader::~QNmeaReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNmeaReaderD1Ev(QNmeaReader *self) {
  delete self;
}

//  void QNmeaReader::readAvailableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNmeaReader17readAvailableDataEv(QNmeaReader *self) {
  self->readAvailableData();
}

//  a Python function taken by a CuteQNmeaReader, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaReader(
    QNmeaReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaReader *>(self)->take(key, call);
}
