//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qpieslice.h>
#include <QtCore/qlist.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/private/declarativepieseries_p.h>
#include <QtCharts/QPieSlice>
#include <QtCharts/QVPieModelMapper>
#include <QtCharts/QHPieModelMapper>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 55, as _ZN20DeclarativePieSeries10classBeginEv
inline void DeclarativePieSeries::classBegin()
{
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 59, as _ZN20DeclarativePieSeries17componentCompleteEv
inline void DeclarativePieSeries::componentComplete()
{
    const auto childlist = children();
    for (QObject *child : childlist) {
        if (qobject_cast<QPieSlice *>(child)) {
            QPieSeries::append(qobject_cast<QPieSlice *>(child));
        } else if (qobject_cast<QVPieModelMapper *>(child)) {
            QVPieModelMapper *mapper = qobject_cast<QVPieModelMapper *>(child);
            mapper->setSeries(this);
        } else if (qobject_cast<QHPieModelMapper *>(child)) {
            QHPieModelMapper *mapper = qobject_cast<QHPieModelMapper *>(child);
            mapper->setSeries(this);
        }
    }
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 75, as _ZN20DeclarativePieSeries14seriesChildrenEv
inline QQmlListProperty<QObject> DeclarativePieSeries::seriesChildren()
{
    return QQmlListProperty<QObject>(this, 0, &DeclarativePieSeries::appendSeriesChildren ,0,0,0);
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 87, as _ZN20DeclarativePieSeries2atEi
inline QPieSlice *DeclarativePieSeries::at(int index)
{
    const QList<QPieSlice *> sliceList = slices();
    if (index >= 0 && index < sliceList.size())
        return sliceList.at(index);

    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 96, as _ZN20DeclarativePieSeries4findE7QString
inline QPieSlice *DeclarativePieSeries::find(QString label)
{
    const QList<QPieSlice *> sliceList = slices();
    for (auto *slice : sliceList) {
        if (slice->label() == label)
            return slice;
    }
    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 106, as _ZN20DeclarativePieSeries6appendE7QStringd
inline DeclarativePieSlice *DeclarativePieSeries::append(QString label, qreal value)
{
    DeclarativePieSlice *slice = new DeclarativePieSlice(this);
    slice->setLabel(label);
    slice->setValue(value);
    if (QPieSeries::append(slice))
        return slice;
    delete slice;
    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 117, as _ZN20DeclarativePieSeries6removeEP9QPieSlice
inline bool DeclarativePieSeries::remove(QPieSlice *slice)
{
    return QPieSeries::remove(slice);
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 80, as _ZN20DeclarativePieSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_
inline void DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject> * list, QObject *element)
{
    // Empty implementation; the children are parsed in componentComplete instead
    Q_UNUSED(list);
    Q_UNUSED(element);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *DeclarativePieSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20DeclarativePieSeries10metaObjectEv(
    const DeclarativePieSeries *self) {
  return self->metaObject();
}

//  void *DeclarativePieSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20DeclarativePieSeries11qt_metacastEPKc(
    DeclarativePieSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativePieSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20DeclarativePieSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativePieSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQmlListProperty<QObject> DeclarativePieSeries::seriesChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20DeclarativePieSeries14seriesChildrenEv(
    DeclarativePieSeries *self) {
  return new QQmlListProperty<QObject>(self->seriesChildren());
}

//  QPieSlice *DeclarativePieSeries::at(int index)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN20DeclarativePieSeries2atEi(
    DeclarativePieSeries *self,
    int index) {
  return self->at(index);
}

//  QPieSlice *DeclarativePieSeries::find(QString label)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN20DeclarativePieSeries4findE7QString(
    DeclarativePieSeries *self,
    const QString *label) {
  return self->find(*label);
}

//  DeclarativePieSlice *DeclarativePieSeries::append(QString label, qreal
//      value)
extern "C" Q_DECL_EXPORT
DeclarativePieSlice *ritual_ZN20DeclarativePieSeries6appendE7QStringd(
    DeclarativePieSeries *self,
    const QString *label,
    qreal value) {
  return self->append(*label, value);
}

//  bool DeclarativePieSeries::remove(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20DeclarativePieSeries6removeEP9QPieSlice(
    DeclarativePieSeries *self,
    QPieSlice *slice) {
  return self->remove(slice);
}

//  void DeclarativePieSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries5clearEv(DeclarativePieSeries *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clear()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clear()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries10classBeginEv(
    DeclarativePieSeries *self) {
  self->classBegin();
}

//  void DeclarativePieSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries17componentCompleteEv(
    DeclarativePieSeries *self) {
  self->componentComplete();
}

//  void DeclarativePieSeries::sliceAdded(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries10sliceAddedEP9QPieSlice(
    DeclarativePieSeries *self,
    QPieSlice *slice) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sliceAdded(QPieSlice *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sliceAdded(QPieSlice *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&slice)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::sliceRemoved(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries12sliceRemovedEP9QPieSlice(
    DeclarativePieSeries *self,
    QPieSlice *slice) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sliceRemoved(QPieSlice *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sliceRemoved(QPieSlice *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&slice)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::handleAdded(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries11handleAddedERK5QListIP9QPieSliceE(
    DeclarativePieSeries *self,
    const QList<QPieSlice *> *slices) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleAdded(const QList<QPieSlice *> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleAdded(const QList<QPieSlice *> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(slices)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::handleRemoved(const QList<QPieSlice *>
//      &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries13handleRemovedERK5QListIP9QPieSliceE(
    DeclarativePieSeries *self,
    const QList<QPieSlice *> *slices) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleRemoved(const QList<QPieSlice *> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleRemoved(const QList<QPieSlice *> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(slices)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject>
//      *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativePieSeries::appendSeriesChildren(list, element);
}

//  DeclarativePieSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativePieSeries_QQmlParserStatus(
    DeclarativePieSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void DeclarativePieSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20DeclarativePieSeries10classBeginEv(
    DeclarativePieSeries *self) {
  self->DeclarativePieSeries::classBegin();
}

//  void DeclarativePieSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20DeclarativePieSeries17componentCompleteEv(
    DeclarativePieSeries *self) {
  self->DeclarativePieSeries::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativePieSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativePieSeries__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_pie_chart)
