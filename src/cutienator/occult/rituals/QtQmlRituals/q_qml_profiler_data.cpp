//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QQmlProfilerData::QQmlProfilerData(qint64 time, int messageType,
//      RangeType detailType, quintptr locationId)
extern "C" Q_DECL_EXPORT
QQmlProfilerData *ritual_ZN16QQmlProfilerDataC1ExiN23QQmlProfilerDefinitions9RangeTypeEy(
    qint64 time,
    int messageType,
    QQmlProfilerDefinitions::RangeType detailType,
    quintptr locationId) {
  return new QQmlProfilerData(time, messageType, detailType, locationId);
}

//  QQmlProfilerData::~QQmlProfilerData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlProfilerDataD1Ev(QQmlProfilerData *self) {
  delete self;
}

//  QList<QQmlProfilerData>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlProfilerData> *ritual_list_make_QQmlProfilerData() {
  return new QList<QQmlProfilerData>();
}

//  void QList<QQmlProfilerData>::append(const QQmlProfilerData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlProfilerData(
    QList<QQmlProfilerData> *self,
    const QQmlProfilerData *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlProfilerData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlProfilerData(
    const QList<QQmlProfilerData> *self) {
  return self->size();
}

//  const QQmlProfilerData &QList<QQmlProfilerData>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlProfilerData *ritual_list_at_QQmlProfilerData(
    const QList<QQmlProfilerData> *self,
    long long index) {
  return new QQmlProfilerData(self->at(index));
}

//  QList<QQmlProfilerData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlProfilerData(QList<QQmlProfilerData> *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
