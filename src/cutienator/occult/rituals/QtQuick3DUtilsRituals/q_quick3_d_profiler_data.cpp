//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQuick3DUtils/qtquick3dutilsexports.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuick3DProfilerData::QQuick3DProfilerData()
extern "C" Q_DECL_EXPORT
QQuick3DProfilerData *ritual_ZN20QQuick3DProfilerDataC1Ev() {
  return new QQuick3DProfilerData();
}

//  QQuick3DProfilerData::QQuick3DProfilerData(qint64 time, int messageType,
//      int detailType, qint64 d1, qint64 d2)
extern "C" Q_DECL_EXPORT
QQuick3DProfilerData *ritual_ZN20QQuick3DProfilerDataC1Exiixx(
    qint64 time,
    int messageType,
    int detailType,
    qint64 d1,
    qint64 d2) {
  return new QQuick3DProfilerData(time, messageType, detailType, d1, d2);
}

//  QQuick3DProfilerData::QQuick3DProfilerData(qint64 time, int messageType,
//      int detailType, qint64 d1, qint64 d2, const QList<int> &ids)
extern "C" Q_DECL_EXPORT
QQuick3DProfilerData *ritual_ZN20QQuick3DProfilerDataC1ExiixxRK5QListIiE(
    qint64 time,
    int messageType,
    int detailType,
    qint64 d1,
    qint64 d2,
    const QList<int> *ids) {
  return new QQuick3DProfilerData(
      time,
      messageType,
      detailType,
      d1,
      d2,
      *ids);
}

//  QQuick3DProfilerData::~QQuick3DProfilerData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DProfilerDataD1Ev(QQuick3DProfilerData *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
