//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativeboxplotseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeboxplotseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  const QMetaObject *DeclarativeBoxSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17DeclarativeBoxSet10metaObjectEv(
    const DeclarativeBoxSet *self) {
  return self->metaObject();
}

//  QString DeclarativeBoxSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17DeclarativeBoxSet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeBoxSet::tr(s, c, n));
}

//  DeclarativeBoxSet::DeclarativeBoxSet(const QString label, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
DeclarativeBoxSet *ritual_ZN17DeclarativeBoxSetC1E7QStringP7QObject(
    const QString *label,
    QObject *parent) {
  return new DeclarativeBoxSet(*label, parent);
}

//  QVariantList DeclarativeBoxSet::values()
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN17DeclarativeBoxSet6valuesEv(
    DeclarativeBoxSet *self) {
  return new QList<QVariant>(self->values());
}

//  void DeclarativeBoxSet::setValues(QVariantList values)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBoxSet9setValuesE5QListI8QVariantE(
    DeclarativeBoxSet *self,
    const QList<QVariant> *values) {
  self->setValues(*values);
}

//  QString DeclarativeBoxSet::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DeclarativeBoxSet13brushFilenameEv(
    const DeclarativeBoxSet *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativeBoxSet::setBrushFilename(const QString &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBoxSet16setBrushFilenameERK7QString(
    DeclarativeBoxSet *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  void DeclarativeBoxSet::append(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBoxSet6appendEd(
    DeclarativeBoxSet *self,
    qreal value) {
  self->append(value);
}

//  void DeclarativeBoxSet::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBoxSet5clearEv(DeclarativeBoxSet *self) {
  self->clear();
}

//  qreal DeclarativeBoxSet::at(int index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17DeclarativeBoxSet2atEi(DeclarativeBoxSet *self, int index) {
  return self->at(index);
}

//  void DeclarativeBoxSet::setValue(int index, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBoxSet8setValueEid(
    DeclarativeBoxSet *self,
    int index,
    qreal value) {
  self->setValue(index, value);
}

//  void DeclarativeBoxSet::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DeclarativeBoxSet18handleBrushChangedEv(
    DeclarativeBoxSet *self) {
  self->handleBrushChanged();
}

#endif  // QT_CONFIG(charts_boxplot_chart)
