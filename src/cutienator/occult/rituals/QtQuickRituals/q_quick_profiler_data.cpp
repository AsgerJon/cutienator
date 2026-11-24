//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  QQuickProfilerData::QQuickProfilerData()
extern "C" Q_DECL_EXPORT
QQuickProfilerData *ritual_ZN18QQuickProfilerDataC1Ev() {
  return new QQuickProfilerData();
}

//  QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType, int
//      detailType, const QUrl &url, int x, int y, int framerate, int count)
extern "C" Q_DECL_EXPORT
QQuickProfilerData *ritual_ZN18QQuickProfilerDataC1ExiiRK4QUrliiii(
    qint64 time,
    int messageType,
    int detailType,
    const QUrl *url,
    int x,
    int y,
    int framerate,
    int count) {
  return new QQuickProfilerData(
      time,
      messageType,
      detailType,
      *url,
      x,
      y,
      framerate,
      count);
}

//  QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType, int
//      detailType, int framerateOrInputType, int countOrInputA, int
//      threadIdOrInputB)
extern "C" Q_DECL_EXPORT
QQuickProfilerData *ritual_ZN18QQuickProfilerDataC1Exiiiii(
    qint64 time,
    int messageType,
    int detailType,
    int framerateOrInputType,
    int countOrInputA,
    int threadIdOrInputB) {
  return new QQuickProfilerData(
      time,
      messageType,
      detailType,
      framerateOrInputType,
      countOrInputA,
      threadIdOrInputB);
}

//  QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType, int
//      detailType, qint64 d1, qint64 d2, qint64 d3, qint64 d4, qint64 d5)
extern "C" Q_DECL_EXPORT
QQuickProfilerData *ritual_ZN18QQuickProfilerDataC1Exiixxxxx(
    qint64 time,
    int messageType,
    int detailType,
    qint64 d1,
    qint64 d2,
    qint64 d3,
    qint64 d4,
    qint64 d5) {
  return new QQuickProfilerData(
      time,
      messageType,
      detailType,
      d1,
      d2,
      d3,
      d4,
      d5);
}

//  QQuickProfilerData::~QQuickProfilerData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickProfilerDataD1Ev(QQuickProfilerData *self) {
  delete self;
}

//  QList<QQuickProfilerData>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickProfilerData> *ritual_list_make_QQuickProfilerData() {
  return new QList<QQuickProfilerData>();
}

//  void QList<QQuickProfilerData>::append(const QQuickProfilerData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickProfilerData(
    QList<QQuickProfilerData> *self,
    const QQuickProfilerData *element) {
  self->append(*element);
}

//  qsizetype QList<QQuickProfilerData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickProfilerData(
    const QList<QQuickProfilerData> *self) {
  return self->size();
}

//  const QQuickProfilerData &QList<QQuickProfilerData>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuickProfilerData *ritual_list_at_QQuickProfilerData(
    const QList<QQuickProfilerData> *self,
    long long index) {
  return new QQuickProfilerData(self->at(index));
}

//  QList<QQuickProfilerData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickProfilerData(QList<QQuickProfilerData> *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
