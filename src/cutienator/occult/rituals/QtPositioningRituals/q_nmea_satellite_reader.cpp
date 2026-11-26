//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qnmeasatelliteinfosource.h>
#include <QtPositioning/private/qnmeasatelliteinfosource_p.h>
#include <QtPositioning/private/qgeosatelliteinfo_p.h>
#include <QtPositioning/private/qgeosatelliteinfosource_p.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtCore/QIODevice>
#include <QtCore/QBasicTimer>
#include <QtCore/QTimerEvent>
#include <QtCore/QTimer>
#include <array>
#include <QtCore/QDebug>
#include <QtCore/QtNumeric>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 834, as _ZN20QNmeaSatelliteReaderD2Ev
inline QNmeaSatelliteReader::~QNmeaSatelliteReader()
{
}

//  from ../qtpositioning/src/positioning/qnmeasatelliteinfosource.cpp, line 829, as _ZN20QNmeaSatelliteReaderC1EP31QNmeaSatelliteInfoSourcePrivate
inline QNmeaSatelliteReader::QNmeaSatelliteReader(QNmeaSatelliteInfoSourcePrivate *sourcePrivate)
    : m_proxy(sourcePrivate)
{
}
//  -----------------------------------------------------------------------

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

//  QNmeaSatelliteReader::QNmeaSatelliteReader(QNmeaSatelliteInfoSourcePrivat
//      e *sourcePrivate)
extern "C" Q_DECL_EXPORT
QNmeaSatelliteReader *ritual_ZN20QNmeaSatelliteReaderC1EP31QNmeaSatelliteInfoSourcePrivate(
    QNmeaSatelliteInfoSourcePrivate *sourcePrivate) {
  return new CuteQNmeaSatelliteReader(sourcePrivate);
}

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
