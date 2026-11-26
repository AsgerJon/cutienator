//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  const QMetaObject *DeclarativeBarSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17DeclarativeBarSet10metaObjectEv(
    const DeclarativeBarSet *self) {
  return self->metaObject();
}

//  void *DeclarativeBarSet::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17DeclarativeBarSet11qt_metacastEPKc(
    DeclarativeBarSet *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeBarSet::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17DeclarativeBarSet11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeBarSet *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeBarSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17DeclarativeBarSet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeBarSet::tr(s, c, n));
}

//  DeclarativeBarSet::DeclarativeBarSet(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN17DeclarativeBarSetC1EP7QObject(
    QObject *parent) {
  return new DeclarativeBarSet(parent);
}

//  QVariantList DeclarativeBarSet::values()
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN17DeclarativeBarSet6valuesEv(
    DeclarativeBarSet *self) {
  return new QList<QVariant>(self->values());
}

//  void DeclarativeBarSet::setValues(QVariantList values)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet9setValuesE5QListI8QVariantE(
    DeclarativeBarSet *self,
    const QList<QVariant> *values) {
  self->setValues(*values);
}

//  qreal DeclarativeBarSet::borderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17DeclarativeBarSet11borderWidthEv(
    const DeclarativeBarSet *self) {
  return self->borderWidth();
}

//  void DeclarativeBarSet::setBorderWidth(qreal borderWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet14setBorderWidthEd(
    DeclarativeBarSet *self,
    qreal borderWidth) {
  self->setBorderWidth(borderWidth);
}

//  QString DeclarativeBarSet::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DeclarativeBarSet13brushFilenameEv(
    const DeclarativeBarSet *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativeBarSet::setBrushFilename(const QString &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet16setBrushFilenameERK7QString(
    DeclarativeBarSet *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  void DeclarativeBarSet::append(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet6appendEd(
    DeclarativeBarSet *self,
    qreal value) {
  self->append(value);
}

//  void DeclarativeBarSet::remove(const int index, const int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet6removeEii(
    DeclarativeBarSet *self,
    int index,
    int count) {
  self->remove(index, count);
}

//  void DeclarativeBarSet::replace(int index, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet7replaceEid(
    DeclarativeBarSet *self,
    int index,
    qreal value) {
  self->replace(index, value);
}

//  qreal DeclarativeBarSet::at(int index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17DeclarativeBarSet2atEi(DeclarativeBarSet *self, int index) {
  return self->at(index);
}

//  void DeclarativeBarSet::countChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet12countChangedEi(
    DeclarativeBarSet *self,
    int count) {
  self->countChanged(count);
}

//  void DeclarativeBarSet::borderWidthChanged(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet18borderWidthChangedEd(
    DeclarativeBarSet *self,
    qreal width) {
  self->borderWidthChanged(width);
}

//  void DeclarativeBarSet::brushFilenameChanged(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet20brushFilenameChangedERK7QString(
    DeclarativeBarSet *self,
    const QString *brushFilename) {
  self->brushFilenameChanged(*brushFilename);
}

//  void DeclarativeBarSet::handleCountChanged(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet18handleCountChangedEii(
    DeclarativeBarSet *self,
    int index,
    int count) {
  self->handleCountChanged(index, count);
}

//  void DeclarativeBarSet::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBarSet18handleBrushChangedEv(
    DeclarativeBarSet *self) {
  self->handleBrushChanged();
}

#endif  // QT_CONFIG(charts_bar_chart)
