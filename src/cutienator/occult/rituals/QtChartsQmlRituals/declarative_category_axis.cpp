//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 78, as _ZN23DeclarativeCategoryAxis16endValueLessThanERKSt4pairI7QStringdES4_
inline bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString, qreal> &value1, const QPair<QString, qreal> &value2)
{
    return value1.second < value2.second;
}

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

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 110, as _ZNK23DeclarativeCategoryAxis14labelsPositionEv
inline DeclarativeCategoryAxis::AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition() const
{
    return (DeclarativeCategoryAxis::AxisLabelsPosition) QCategoryAxis::labelsPosition();
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 88, as _ZN23DeclarativeCategoryAxis6appendERK7QStringd
inline void DeclarativeCategoryAxis::append(const QString &label, qreal categoryEndValue)
{
    QCategoryAxis::append(label, categoryEndValue);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 93, as _ZN23DeclarativeCategoryAxis6removeERK7QString
inline void DeclarativeCategoryAxis::remove(const QString &label)
{
    QCategoryAxis::remove(label);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 98, as _ZN23DeclarativeCategoryAxis7replaceERK7QStringS2_
inline void DeclarativeCategoryAxis::replace(const QString &oldLabel, const QString &newLabel)
{
    QCategoryAxis::replaceLabel(oldLabel, newLabel);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *DeclarativeCategoryAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23DeclarativeCategoryAxis10metaObjectEv(
    const DeclarativeCategoryAxis *self) {
  return self->metaObject();
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

//  void DeclarativeCategoryAxis::append(const QString &label, qreal
//      categoryEndValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis6appendERK7QStringd(
    DeclarativeCategoryAxis *self,
    const QString *label,
    qreal categoryEndValue) {
  self->append(*label, categoryEndValue);
}

//  void DeclarativeCategoryAxis::remove(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis6removeERK7QString(
    DeclarativeCategoryAxis *self,
    const QString *label) {
  self->remove(*label);
}

//  void DeclarativeCategoryAxis::replace(const QString &oldLabel, const
//      QString &newLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis7replaceERK7QStringS2_(
    DeclarativeCategoryAxis *self,
    const QString *oldLabel,
    const QString *newLabel) {
  self->replace(*oldLabel, *newLabel);
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
