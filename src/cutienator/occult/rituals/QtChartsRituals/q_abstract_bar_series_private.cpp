//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qabstractbarseries_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qabstractbarseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qabstractbarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCharts/qbarset.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QAbstractBarSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAbstractBarSeriesPrivate10metaObjectEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QAbstractBarSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QAbstractBarSeriesPrivate11qt_metacastEPKc(
    QAbstractBarSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractBarSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QAbstractBarSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractBarSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractBarSeriesPrivate::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QAbstractBarSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractBarSeriesPrivate::tr(s, c, n));
}

//  int QAbstractBarSeriesPrivate::categoryCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAbstractBarSeriesPrivate13categoryCountEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->categoryCount();
}

//  void QAbstractBarSeriesPrivate::setBarWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate11setBarWidthEd(
    QAbstractBarSeriesPrivate *self,
    qreal width) {
  self->setBarWidth(width);
}

//  qreal QAbstractBarSeriesPrivate::barWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QAbstractBarSeriesPrivate8barWidthEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->barWidth();
}

//  void QAbstractBarSeriesPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate10setVisibleEb(
    QAbstractBarSeriesPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QAbstractBarSeriesPrivate::setLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate16setLabelsVisibleEb(
    QAbstractBarSeriesPrivate *self,
    bool visible) {
  self->setLabelsVisible(visible);
}

//  void QAbstractBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate16initializeDomainEv(
    QAbstractBarSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QAbstractBarSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate14initializeAxesEv(
    QAbstractBarSeriesPrivate *self) {
  self->initializeAxes();
}

//  void
//      QAbstractBarSeriesPrivate::initializeAnimations(QChart::AnimationOpti
//      ons options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QAbstractBarSeriesPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
}

//  void QAbstractBarSeriesPrivate::initializeTheme(int index, ChartTheme
//      *theme, bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QAbstractBarSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  QList<QLegendMarker *>
//      QAbstractBarSeriesPrivate::createLegendMarkers(QLegend *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN25QAbstractBarSeriesPrivate19createLegendMarkersEP7QLegend(
    QAbstractBarSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType
//      QAbstractBarSeriesPrivate::defaultAxisType(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK25QAbstractBarSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QAbstractBarSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->defaultAxisType(orientation);
}

//  QAbstractAxis
//      *QAbstractBarSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK25QAbstractBarSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QAbstractBarSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  bool QAbstractBarSeriesPrivate::append(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractBarSeriesPrivate6appendEP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    QBarSet *set) {
  return self->append(set);
}

//  bool QAbstractBarSeriesPrivate::remove(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractBarSeriesPrivate6removeEP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    QBarSet *set) {
  return self->remove(set);
}

//  bool QAbstractBarSeriesPrivate::append(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractBarSeriesPrivate6appendERK5QListIP7QBarSetE(
    QAbstractBarSeriesPrivate *self,
    const QList<QBarSet *> *sets) {
  return self->append(*sets);
}

//  bool QAbstractBarSeriesPrivate::remove(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractBarSeriesPrivate6removeERK5QListIP7QBarSetE(
    QAbstractBarSeriesPrivate *self,
    const QList<QBarSet *> *sets) {
  return self->remove(*sets);
}

//  bool QAbstractBarSeriesPrivate::insert(int index, QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractBarSeriesPrivate6insertEiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    QBarSet *set) {
  return self->insert(index, set);
}

//  QBarSet *QAbstractBarSeriesPrivate::barsetAt(int index)
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN25QAbstractBarSeriesPrivate8barsetAtEi(
    QAbstractBarSeriesPrivate *self,
    int index) {
  return self->barsetAt(index);
}

//  qreal QAbstractBarSeriesPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate3minEv(
    QAbstractBarSeriesPrivate *self) {
  return self->min();
}

//  qreal QAbstractBarSeriesPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate3maxEv(
    QAbstractBarSeriesPrivate *self) {
  return self->max();
}

//  qreal QAbstractBarSeriesPrivate::valueAt(int set, int category)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate7valueAtEii(
    QAbstractBarSeriesPrivate *self,
    int set,
    int category) {
  return self->valueAt(set, category);
}

//  qreal QAbstractBarSeriesPrivate::percentageAt(int set, int category)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate12percentageAtEii(
    QAbstractBarSeriesPrivate *self,
    int set,
    int category) {
  return self->percentageAt(set, category);
}

//  qreal QAbstractBarSeriesPrivate::categorySum(int category)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate11categorySumEi(
    QAbstractBarSeriesPrivate *self,
    int category) {
  return self->categorySum(category);
}

//  qreal QAbstractBarSeriesPrivate::absoluteCategorySum(int category)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate19absoluteCategorySumEi(
    QAbstractBarSeriesPrivate *self,
    int category) {
  return self->absoluteCategorySum(category);
}

//  qreal QAbstractBarSeriesPrivate::maxCategorySum()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate14maxCategorySumEv(
    QAbstractBarSeriesPrivate *self) {
  return self->maxCategorySum();
}

//  qreal QAbstractBarSeriesPrivate::minX()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate4minXEv(
    QAbstractBarSeriesPrivate *self) {
  return self->minX();
}

//  qreal QAbstractBarSeriesPrivate::maxX()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate4maxXEv(
    QAbstractBarSeriesPrivate *self) {
  return self->maxX();
}

//  qreal QAbstractBarSeriesPrivate::categoryTop(int category)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate11categoryTopEi(
    QAbstractBarSeriesPrivate *self,
    int category) {
  return self->categoryTop(category);
}

//  qreal QAbstractBarSeriesPrivate::categoryBottom(int category)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate14categoryBottomEi(
    QAbstractBarSeriesPrivate *self,
    int category) {
  return self->categoryBottom(category);
}

//  qreal QAbstractBarSeriesPrivate::top()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate3topEv(
    QAbstractBarSeriesPrivate *self) {
  return self->top();
}

//  qreal QAbstractBarSeriesPrivate::bottom()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN25QAbstractBarSeriesPrivate6bottomEv(
    QAbstractBarSeriesPrivate *self) {
  return self->bottom();
}

//  bool QAbstractBarSeriesPrivate::blockBarUpdate()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractBarSeriesPrivate14blockBarUpdateEv(
    QAbstractBarSeriesPrivate *self) {
  return self->blockBarUpdate();
}

//  qreal QAbstractBarSeriesPrivate::labelsAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QAbstractBarSeriesPrivate11labelsAngleEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->labelsAngle();
}

//  void QAbstractBarSeriesPrivate::setVisualsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate15setVisualsDirtyEb(
    QAbstractBarSeriesPrivate *self,
    bool dirty) {
  self->setVisualsDirty(dirty);
}

//  bool QAbstractBarSeriesPrivate::visualsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractBarSeriesPrivate12visualsDirtyEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->visualsDirty();
}

//  void QAbstractBarSeriesPrivate::setLabelsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate14setLabelsDirtyEb(
    QAbstractBarSeriesPrivate *self,
    bool dirty) {
  self->setLabelsDirty(dirty);
}

//  bool QAbstractBarSeriesPrivate::labelsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractBarSeriesPrivate11labelsDirtyEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->labelsDirty();
}

//  void QAbstractBarSeriesPrivate::clicked(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate7clickedEiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    QBarSet *barset) {
  self->clicked(index, barset);
}

//  void QAbstractBarSeriesPrivate::pressed(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate7pressedEiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    QBarSet *barset) {
  self->pressed(index, barset);
}

//  void QAbstractBarSeriesPrivate::released(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate8releasedEiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    QBarSet *barset) {
  self->released(index, barset);
}

//  void QAbstractBarSeriesPrivate::doubleClicked(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate13doubleClickedEiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    QBarSet *barset) {
  self->doubleClicked(index, barset);
}

//  void QAbstractBarSeriesPrivate::updatedBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate11updatedBarsEv(
    QAbstractBarSeriesPrivate *self) {
  self->updatedBars();
}

//  void QAbstractBarSeriesPrivate::updatedLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate13updatedLayoutEv(
    QAbstractBarSeriesPrivate *self) {
  self->updatedLayout();
}

//  void QAbstractBarSeriesPrivate::restructuredBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate16restructuredBarsEv(
    QAbstractBarSeriesPrivate *self) {
  self->restructuredBars();
}

//  void QAbstractBarSeriesPrivate::labelsVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate20labelsVisibleChangedEb(
    QAbstractBarSeriesPrivate *self,
    bool visible) {
  self->labelsVisibleChanged(visible);
}

//  void QAbstractBarSeriesPrivate::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate14visibleChangedEv(
    QAbstractBarSeriesPrivate *self) {
  self->visibleChanged();
}

//  void QAbstractBarSeriesPrivate::setValueChanged(int index, QBarSet
//      *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate15setValueChangedEiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    QBarSet *barset) {
  self->setValueChanged(index, barset);
}

//  void QAbstractBarSeriesPrivate::setValueAdded(int index, int count,
//      QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate13setValueAddedEiiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    int count,
    QBarSet *barset) {
  self->setValueAdded(index, count, barset);
}

//  void QAbstractBarSeriesPrivate::setValueRemoved(int index, int count,
//      QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate15setValueRemovedEiiP7QBarSet(
    QAbstractBarSeriesPrivate *self,
    int index,
    int count,
    QBarSet *barset) {
  self->setValueRemoved(index, count, barset);
}

//  void QAbstractBarSeriesPrivate::handleSetValueChange(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate20handleSetValueChangeEi(
    QAbstractBarSeriesPrivate *self,
    int index) {
  self->handleSetValueChange(index);
}

//  void QAbstractBarSeriesPrivate::handleSetValueAdd(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate17handleSetValueAddEii(
    QAbstractBarSeriesPrivate *self,
    int index,
    int count) {
  self->handleSetValueAdd(index, count);
}

//  void QAbstractBarSeriesPrivate::handleSetValueRemove(int index, int
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate20handleSetValueRemoveEii(
    QAbstractBarSeriesPrivate *self,
    int index,
    int count) {
  self->handleSetValueRemove(index, count);
}

//  void QAbstractBarSeriesPrivate::populateCategories(QBarCategoryAxis
//      *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractBarSeriesPrivate18populateCategoriesEP16QBarCategoryAxis(
    QAbstractBarSeriesPrivate *self,
    QBarCategoryAxis *axis) {
  self->populateCategories(axis);
}

//  QAbstractBarSeries *QAbstractBarSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_ZN25QAbstractBarSeriesPrivate6q_funcEv(
    QAbstractBarSeriesPrivate *self) {
  return self->q_func();
}

//  const QAbstractBarSeries *QAbstractBarSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractBarSeries *ritual_ZNK25QAbstractBarSeriesPrivate6q_funcEv(
    const QAbstractBarSeriesPrivate *self) {
  return self->q_func();
}

//  void QAbstractBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAbstractBarSeriesPrivate16initializeDomainEv(
    QAbstractBarSeriesPrivate *self) {
  self->QAbstractBarSeriesPrivate::initializeDomain();
}

//  void QAbstractBarSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAbstractBarSeriesPrivate14initializeAxesEv(
    QAbstractBarSeriesPrivate *self) {
  self->QAbstractBarSeriesPrivate::initializeAxes();
}

//  void QAbstractBarSeriesPrivate::initializeTheme(int index, ChartTheme
//      *theme, bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAbstractBarSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QAbstractBarSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QAbstractBarSeriesPrivate::initializeTheme(index, theme, forced);
}

//  QAbstractAxis::AxisType
//      QAbstractBarSeriesPrivate::defaultAxisType(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK25QAbstractBarSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QAbstractBarSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QAbstractBarSeriesPrivate::defaultAxisType(orientation);
}

//  QAbstractAxis
//      *QAbstractBarSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_own_ZNK25QAbstractBarSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QAbstractBarSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QAbstractBarSeriesPrivate::createDefaultAxis(orientation);
}

#endif  // QT_CONFIG(charts_bar_chart)
