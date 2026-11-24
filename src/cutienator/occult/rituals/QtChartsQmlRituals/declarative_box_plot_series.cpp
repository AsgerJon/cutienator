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

//  const QMetaObject *DeclarativeBoxPlotSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24DeclarativeBoxPlotSeries10metaObjectEv(
    const DeclarativeBoxPlotSeries *self) {
  return self->metaObject();
}

//  QString DeclarativeBoxPlotSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24DeclarativeBoxPlotSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeBoxPlotSeries::tr(s, c, n));
}

//  DeclarativeBoxPlotSeries::DeclarativeBoxPlotSeries(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
DeclarativeBoxPlotSeries *ritual_ZN24DeclarativeBoxPlotSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new DeclarativeBoxPlotSeries(parent);
}

//  QAbstractAxis *DeclarativeBoxPlotSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeBoxPlotSeries5axisXEv(
    DeclarativeBoxPlotSeries *self) {
  return self->axisX();
}

//  void DeclarativeBoxPlotSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries8setAxisXEP13QAbstractAxis(
    DeclarativeBoxPlotSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeBoxPlotSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeBoxPlotSeries5axisYEv(
    DeclarativeBoxPlotSeries *self) {
  return self->axisY();
}

//  void DeclarativeBoxPlotSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries8setAxisYEP13QAbstractAxis(
    DeclarativeBoxPlotSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeBoxPlotSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeBoxPlotSeries8axisXTopEv(
    DeclarativeBoxPlotSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeBoxPlotSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeBoxPlotSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeBoxPlotSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeBoxPlotSeries10axisYRightEv(
    DeclarativeBoxPlotSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeBoxPlotSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeBoxPlotSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QString DeclarativeBoxPlotSeries::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24DeclarativeBoxPlotSeries13brushFilenameEv(
    const DeclarativeBoxPlotSeries *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativeBoxPlotSeries::setBrushFilename(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries16setBrushFilenameERK7QString(
    DeclarativeBoxPlotSeries *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  DeclarativeBoxSet *DeclarativeBoxPlotSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeBoxSet *ritual_ZN24DeclarativeBoxPlotSeries2atEi(
    DeclarativeBoxPlotSeries *self,
    int index) {
  return self->at(index);
}

//  DeclarativeBoxSet *DeclarativeBoxPlotSeries::append(const QString label,
//      QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBoxSet *ritual_ZN24DeclarativeBoxPlotSeries6appendE7QString5QListI8QVariantE(
    DeclarativeBoxPlotSeries *self,
    const QString *label,
    const QList<QVariant> *values) {
  return self->append(*label, *values);
}

//  void DeclarativeBoxPlotSeries::append(DeclarativeBoxSet *box)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries6appendEP17DeclarativeBoxSet(
    DeclarativeBoxPlotSeries *self,
    DeclarativeBoxSet *box) {
  self->append(box);
}

//  DeclarativeBoxSet *DeclarativeBoxPlotSeries::insert(int index, const
//      QString label, QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBoxSet *ritual_ZN24DeclarativeBoxPlotSeries6insertEi7QString5QListI8QVariantE(
    DeclarativeBoxPlotSeries *self,
    int index,
    const QString *label,
    const QList<QVariant> *values) {
  return self->insert(index, *label, *values);
}

//  bool DeclarativeBoxPlotSeries::remove(DeclarativeBoxSet *box)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24DeclarativeBoxPlotSeries6removeEP17DeclarativeBoxSet(
    DeclarativeBoxPlotSeries *self,
    DeclarativeBoxSet *box) {
  return self->remove(box);
}

//  void DeclarativeBoxPlotSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries5clearEv(
    DeclarativeBoxPlotSeries *self) {
  self->clear();
}

//  void DeclarativeBoxPlotSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries10classBeginEv(
    DeclarativeBoxPlotSeries *self) {
  self->classBegin();
}

//  void DeclarativeBoxPlotSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries17componentCompleteEv(
    DeclarativeBoxPlotSeries *self) {
  self->componentComplete();
}

//  void DeclarativeBoxPlotSeries::onHovered(bool status, QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries9onHoveredEbP7QBoxSet(
    DeclarativeBoxPlotSeries *self,
    bool status,
    QBoxSet *boxset) {
  self->onHovered(status, boxset);
}

//  void DeclarativeBoxPlotSeries::onClicked(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries9onClickedEP7QBoxSet(
    DeclarativeBoxPlotSeries *self,
    QBoxSet *boxset) {
  self->onClicked(boxset);
}

//  void DeclarativeBoxPlotSeries::onPressed(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries9onPressedEP7QBoxSet(
    DeclarativeBoxPlotSeries *self,
    QBoxSet *boxset) {
  self->onPressed(boxset);
}

//  void DeclarativeBoxPlotSeries::onReleased(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries10onReleasedEP7QBoxSet(
    DeclarativeBoxPlotSeries *self,
    QBoxSet *boxset) {
  self->onReleased(boxset);
}

//  void DeclarativeBoxPlotSeries::onDoubleClicked(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries15onDoubleClickedEP7QBoxSet(
    DeclarativeBoxPlotSeries *self,
    QBoxSet *boxset) {
  self->onDoubleClicked(boxset);
}

//  void DeclarativeBoxPlotSeries::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeBoxPlotSeries18handleBrushChangedEv(
    DeclarativeBoxPlotSeries *self) {
  self->handleBrushChanged();
}

//  DeclarativeBoxPlotSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeBoxPlotSeries_QQmlParserStatus(
    DeclarativeBoxPlotSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void DeclarativeBoxPlotSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24DeclarativeBoxPlotSeries10classBeginEv(
    DeclarativeBoxPlotSeries *self) {
  self->DeclarativeBoxPlotSeries::classBegin();
}

//  void DeclarativeBoxPlotSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24DeclarativeBoxPlotSeries17componentCompleteEv(
    DeclarativeBoxPlotSeries *self) {
  self->DeclarativeBoxPlotSeries::componentComplete();
}

#endif  // QT_CONFIG(charts_boxplot_chart)
