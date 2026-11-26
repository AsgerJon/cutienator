//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativecandlestickseries_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-25: the header of 'DeclarativeAxes' is
//  included before Qt's header of the class, which only declares
//  'DeclarativeAxes' and then calls its functions inline, so the
//  compiler refused it as an incomplete type. Kept as it is when the
//  generator runs again.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeaxes_p.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativecandlestickseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/QHCandlestickModelMapper>
#include <QtCharts/QVCandlestickModelMapper>
#include <QtChartsQml/private/declarativeaxes_p.h>
#include <QtChartsQml/private/declarativecandlestickseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 98, as _ZNK28DeclarativeCandlestickSeries13brushFilenameEv
inline QString DeclarativeCandlestickSeries::brushFilename() const
{
    return m_brushFilename;
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 103, as _ZN28DeclarativeCandlestickSeries2atEi
inline DeclarativeCandlestickSet *DeclarativeCandlestickSeries::at(int index)
{
    QList<QCandlestickSet *> sets = this->sets();
    if (index >= 0 && index < sets.size())
        return qobject_cast<DeclarativeCandlestickSet *>(sets[index]);

    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 112, as _ZN28DeclarativeCandlestickSeries6appendEP25DeclarativeCandlestickSet
inline bool DeclarativeCandlestickSeries::append(DeclarativeCandlestickSet *set)
{
    return QCandlestickSeries::append(qobject_cast<QCandlestickSet *>(set));
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 117, as _ZN28DeclarativeCandlestickSeries6removeEP25DeclarativeCandlestickSet
inline bool DeclarativeCandlestickSeries::remove(DeclarativeCandlestickSet *set)
{
    return QCandlestickSeries::remove(qobject_cast<QCandlestickSet *>(set));
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 122, as _ZN28DeclarativeCandlestickSeries6appendEddddd
inline bool DeclarativeCandlestickSeries::append(qreal open, qreal high, qreal low, qreal close,
                                          qreal timestamp)
{
    QCandlestickSet *set = new QCandlestickSet(open, high, low, close, timestamp);
    if (!QCandlestickSeries::append(set)) {
        delete set;
        return false;
    }

    return true;
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 134, as _ZN28DeclarativeCandlestickSeries6removeEd
inline bool DeclarativeCandlestickSeries::remove(qreal timestamp)
{
    for (int i = 0; i < count(); ++i) {
        QCandlestickSet *set = sets().at(i);
        if (set->timestamp() == timestamp)
            return QCandlestickSeries::remove(set);
    }

    return false;
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 145, as _ZN28DeclarativeCandlestickSeries6insertEiP25DeclarativeCandlestickSet
inline bool DeclarativeCandlestickSeries::insert(int index, DeclarativeCandlestickSet *set)
{
    return QCandlestickSeries::insert(index, qobject_cast<QCandlestickSet *>(set));
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 150, as _ZN28DeclarativeCandlestickSeries5clearEv
inline void DeclarativeCandlestickSeries::clear()
{
    QCandlestickSeries::clear();
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 155, as _ZN28DeclarativeCandlestickSeries10classBeginEv
inline void DeclarativeCandlestickSeries::classBegin()
{
    // do nothing
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 160, as _ZN28DeclarativeCandlestickSeries17componentCompleteEv
inline void DeclarativeCandlestickSeries::componentComplete()
{
    const auto childlist = children();
    for (QObject *child : childlist) {
        if (qobject_cast<DeclarativeCandlestickSet *>(child)) {
            QCandlestickSeries::append(qobject_cast<DeclarativeCandlestickSet *>(child));
        } else if (qobject_cast<QHCandlestickModelMapper *>(child)) {
            QHCandlestickModelMapper *mapper = qobject_cast<QHCandlestickModelMapper *>(child);
            mapper->setSeries(this);
        } else if (qobject_cast<QVCandlestickModelMapper *>(child)) {
            QVCandlestickModelMapper *mapper = qobject_cast<QVCandlestickModelMapper *>(child);
            mapper->setSeries(this);
        } // else: do nothing
    }
}

//  from ../qtcharts/src/chartsqml2/declarativecandlestickseries.cpp, line 176, as _ZN28DeclarativeCandlestickSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_
inline void DeclarativeCandlestickSeries::appendSeriesChildren(QQmlListProperty<QObject> *list,
                                                        QObject *element)
{
    // Empty implementation; the children are parsed in componentComplete instead
    Q_UNUSED(list);
    Q_UNUSED(element);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *DeclarativeCandlestickSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28DeclarativeCandlestickSeries10metaObjectEv(
    const DeclarativeCandlestickSeries *self) {
  return self->metaObject();
}

//  void *DeclarativeCandlestickSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28DeclarativeCandlestickSeries11qt_metacastEPKc(
    DeclarativeCandlestickSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  void DeclarativeCandlestickSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries8setAxisXEP13QAbstractAxis(
    DeclarativeCandlestickSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeCandlestickSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN28DeclarativeCandlestickSeries5axisXEv(
    DeclarativeCandlestickSeries *self) {
  return self->axisX();
}

//  void DeclarativeCandlestickSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries8setAxisYEP13QAbstractAxis(
    DeclarativeCandlestickSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeCandlestickSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN28DeclarativeCandlestickSeries5axisYEv(
    DeclarativeCandlestickSeries *self) {
  return self->axisY();
}

//  void DeclarativeCandlestickSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeCandlestickSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeCandlestickSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN28DeclarativeCandlestickSeries8axisXTopEv(
    DeclarativeCandlestickSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeCandlestickSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeCandlestickSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QAbstractAxis *DeclarativeCandlestickSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN28DeclarativeCandlestickSeries10axisYRightEv(
    DeclarativeCandlestickSeries *self) {
  return self->axisYRight();
}

//  QString DeclarativeCandlestickSeries::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28DeclarativeCandlestickSeries13brushFilenameEv(
    const DeclarativeCandlestickSeries *self) {
  return new QString(self->brushFilename());
}

//  DeclarativeCandlestickSet *DeclarativeCandlestickSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeCandlestickSet *ritual_ZN28DeclarativeCandlestickSeries2atEi(
    DeclarativeCandlestickSeries *self,
    int index) {
  return self->at(index);
}

//  bool DeclarativeCandlestickSeries::append(DeclarativeCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28DeclarativeCandlestickSeries6appendEP25DeclarativeCandlestickSet(
    DeclarativeCandlestickSeries *self,
    DeclarativeCandlestickSet *set) {
  return self->append(set);
}

//  bool DeclarativeCandlestickSeries::remove(DeclarativeCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28DeclarativeCandlestickSeries6removeEP25DeclarativeCandlestickSet(
    DeclarativeCandlestickSeries *self,
    DeclarativeCandlestickSet *set) {
  return self->remove(set);
}

//  bool DeclarativeCandlestickSeries::append(qreal open, qreal high, qreal
//      low, qreal close, qreal timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28DeclarativeCandlestickSeries6appendEddddd(
    DeclarativeCandlestickSeries *self,
    qreal open,
    qreal high,
    qreal low,
    qreal close,
    qreal timestamp) {
  return self->append(open, high, low, close, timestamp);
}

//  bool DeclarativeCandlestickSeries::remove(qreal timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28DeclarativeCandlestickSeries6removeEd(
    DeclarativeCandlestickSeries *self,
    qreal timestamp) {
  return self->remove(timestamp);
}

//  bool DeclarativeCandlestickSeries::insert(int index,
//      DeclarativeCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28DeclarativeCandlestickSeries6insertEiP25DeclarativeCandlestickSet(
    DeclarativeCandlestickSeries *self,
    int index,
    DeclarativeCandlestickSet *set) {
  return self->insert(index, set);
}

//  void DeclarativeCandlestickSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries5clearEv(
    DeclarativeCandlestickSeries *self) {
  self->clear();
}

//  void DeclarativeCandlestickSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries10classBeginEv(
    DeclarativeCandlestickSeries *self) {
  self->classBegin();
}

//  void DeclarativeCandlestickSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries17componentCompleteEv(
    DeclarativeCandlestickSeries *self) {
  self->componentComplete();
}

//  void DeclarativeCandlestickSeries::appendSeriesChildren(QQmlListProperty<
//      QObject> *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN28DeclarativeCandlestickSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeCandlestickSeries::appendSeriesChildren(list, element);
}

//  DeclarativeCandlestickSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeCandlestickSeries_QQmlParserStatus(
    DeclarativeCandlestickSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void DeclarativeCandlestickSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28DeclarativeCandlestickSeries10classBeginEv(
    DeclarativeCandlestickSeries *self) {
  self->DeclarativeCandlestickSeries::classBegin();
}

//  void DeclarativeCandlestickSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28DeclarativeCandlestickSeries17componentCompleteEv(
    DeclarativeCandlestickSeries *self) {
  self->DeclarativeCandlestickSeries::componentComplete();
}

#endif  // QT_CONFIG(charts_candlestick_chart)
