//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/private/declarativecategoryaxis_p.h>
#include <QtCore/QDebug>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 57, as _ZN23DeclarativeCategoryAxis10classBeginEv
inline void DeclarativeCategoryAxis::classBegin()
{
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 61, as _ZN23DeclarativeCategoryAxis17componentCompleteEv
inline void DeclarativeCategoryAxis::componentComplete()
{
    QList<QPair<QString, qreal> > ranges;
    const auto childlist = children();
    for (QObject *child : childlist) {
        if (qobject_cast<DeclarativeCategoryRange *>(child)) {
            DeclarativeCategoryRange *range = qobject_cast<DeclarativeCategoryRange *>(child);
            ranges.append(QPair<QString, qreal>(range->label(), range->endValue()));
        }
    }

    // Sort and append the range objects according to end value
    std::sort(ranges.begin(), ranges.end(), endValueLessThan);
    for (int i(0); i < ranges.size(); i++)
        append(ranges.at(i).first, ranges.at(i).second);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 88, as _ZN23DeclarativeCategoryAxis6appendERK7QStringd
inline void DeclarativeCategoryAxis::append(const QString &label, qreal categoryEndValue)
{
    QCategoryAxis::append(label, categoryEndValue);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 83, as _ZN23DeclarativeCategoryAxis12axisChildrenEv
inline QQmlListProperty<QObject> DeclarativeCategoryAxis::axisChildren()
{
    return QQmlListProperty<QObject>(this, 0, &DeclarativeCategoryAxis::appendAxisChildren ,0,0,0);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 110, as _ZNK23DeclarativeCategoryAxis14labelsPositionEv
inline DeclarativeCategoryAxis::AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition() const
{
    return (DeclarativeCategoryAxis::AxisLabelsPosition) QCategoryAxis::labelsPosition();
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 78, as _ZN23DeclarativeCategoryAxis16endValueLessThanERKSt4pairI7QStringdES4_
inline bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString, qreal> &value1, const QPair<QString, qreal> &value2)
{
    return value1.second < value2.second;
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 103, as _ZN23DeclarativeCategoryAxis18appendAxisChildrenEP16QQmlListPropertyI7QObjectEPS1_
inline void DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObject> *list, QObject *element)
{
    // Empty implementation; the children are parsed in componentComplete instead
    Q_UNUSED(list);
    Q_UNUSED(element);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *DeclarativeCategoryAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23DeclarativeCategoryAxis10metaObjectEv(
    const DeclarativeCategoryAxis *self) {
  return self->metaObject();
}

//  void *DeclarativeCategoryAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23DeclarativeCategoryAxis11qt_metacastEPKc(
    DeclarativeCategoryAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeCategoryAxis::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23DeclarativeCategoryAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeCategoryAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQmlListProperty<QObject> DeclarativeCategoryAxis::axisChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN23DeclarativeCategoryAxis12axisChildrenEv(
    DeclarativeCategoryAxis *self) {
  return new QQmlListProperty<QObject>(self->axisChildren());
}

//  void DeclarativeCategoryAxis::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis10classBeginEv(
    DeclarativeCategoryAxis *self) {
  self->classBegin();
}

//  void DeclarativeCategoryAxis::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis17componentCompleteEv(
    DeclarativeCategoryAxis *self) {
  self->componentComplete();
}

//  AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition() const
extern "C" Q_DECL_EXPORT
DeclarativeCategoryAxis::AxisLabelsPosition ritual_ZNK23DeclarativeCategoryAxis14labelsPositionEv(
    const DeclarativeCategoryAxis *self) {
  return self->labelsPosition();
}

//  void DeclarativeCategoryAxis::labelsPositionChanged(AxisLabelsPosition
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis21labelsPositionChangedENS_18AxisLabelsPositionE(
    DeclarativeCategoryAxis *self,
    DeclarativeCategoryAxis::AxisLabelsPosition position) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "labelsPositionChanged(AxisLabelsPosition)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "labelsPositionChanged(AxisLabelsPosition)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&position)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativeCategoryAxis::append(const QString &label, qreal
//      categoryEndValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis6appendERK7QStringd(
    DeclarativeCategoryAxis *self,
    const QString *label,
    qreal categoryEndValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "append(const QString &,qreal)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "append(const QString &,qreal)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(label)),
      const_cast<void *>(static_cast<const void *>(&categoryEndValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativeCategoryAxis::remove(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis6removeERK7QString(
    DeclarativeCategoryAxis *self,
    const QString *label) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remove(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remove(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(label)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativeCategoryAxis::replace(const QString &oldLabel, const
//      QString &newLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis7replaceERK7QStringS2_(
    DeclarativeCategoryAxis *self,
    const QString *oldLabel,
    const QString *newLabel) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "replace(const QString &,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "replace(const QString &,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(oldLabel)),
      const_cast<void *>(static_cast<const void *>(newLabel)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString,
//      qreal> &value1, const QPair<QString, qreal> &value2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23DeclarativeCategoryAxis16endValueLessThanERKSt4pairI7QStringdES4_(
    const QPair<QString, qreal> *value1,
    const QPair<QString, qreal> *value2) {
  return DeclarativeCategoryAxis::endValueLessThan(*value1, *value2);
}

//  void
//      DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObject>
//      *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis18appendAxisChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeCategoryAxis::appendAxisChildren(list, element);
}

//  DeclarativeCategoryAxis as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeCategoryAxis_QQmlParserStatus(
    DeclarativeCategoryAxis *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void DeclarativeCategoryAxis::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23DeclarativeCategoryAxis10classBeginEv(
    DeclarativeCategoryAxis *self) {
  self->DeclarativeCategoryAxis::classBegin();
}

//  void DeclarativeCategoryAxis::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23DeclarativeCategoryAxis17componentCompleteEv(
    DeclarativeCategoryAxis *self) {
  self->DeclarativeCategoryAxis::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativeCategoryAxis gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativeCategoryAxis__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
