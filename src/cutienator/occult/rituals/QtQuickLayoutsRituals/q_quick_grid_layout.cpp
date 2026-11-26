//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickGridLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickGridLayout10metaObjectEv(
    const QQuickGridLayout *self) {
  return self->metaObject();
}

//  void *QQuickGridLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickGridLayout11qt_metacastEPKc(
    QQuickGridLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGridLayout::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickGridLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGridLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGridLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickGridLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGridLayout::tr(s, c, n));
}

//  QQuickGridLayout::QQuickGridLayout(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGridLayout *ritual_ZN16QQuickGridLayoutC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickGridLayout(parent);
}

//  qreal QQuickGridLayout::columnSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGridLayout13columnSpacingEv(
    const QQuickGridLayout *self) {
  return self->columnSpacing();
}

//  void QQuickGridLayout::setColumnSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout16setColumnSpacingEd(
    QQuickGridLayout *self,
    qreal spacing) {
  self->setColumnSpacing(spacing);
}

//  qreal QQuickGridLayout::rowSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickGridLayout10rowSpacingEv(
    const QQuickGridLayout *self) {
  return self->rowSpacing();
}

//  void QQuickGridLayout::setRowSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout13setRowSpacingEd(
    QQuickGridLayout *self,
    qreal spacing) {
  self->setRowSpacing(spacing);
}

//  int QQuickGridLayout::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGridLayout7columnsEv(const QQuickGridLayout *self) {
  return self->columns();
}

//  void QQuickGridLayout::setColumns(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout10setColumnsEi(
    QQuickGridLayout *self,
    int columns) {
  self->setColumns(columns);
}

//  int QQuickGridLayout::rows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickGridLayout4rowsEv(const QQuickGridLayout *self) {
  return self->rows();
}

//  void QQuickGridLayout::setRows(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout7setRowsEi(
    QQuickGridLayout *self,
    int rows) {
  self->setRows(rows);
}

//  Flow QQuickGridLayout::flow() const
extern "C" Q_DECL_EXPORT
QQuickGridLayout::Flow ritual_ZNK16QQuickGridLayout4flowEv(
    const QQuickGridLayout *self) {
  return self->flow();
}

//  void QQuickGridLayout::setFlow(Flow flow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout7setFlowENS_4FlowE(
    QQuickGridLayout *self,
    QQuickGridLayout::Flow flow) {
  self->setFlow(flow);
}

//  bool QQuickGridLayout::uniformCellWidths() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGridLayout17uniformCellWidthsEv(
    const QQuickGridLayout *self) {
  return self->uniformCellWidths();
}

//  void QQuickGridLayout::setUniformCellWidths(bool uniformCellWidths)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout20setUniformCellWidthsEb(
    QQuickGridLayout *self,
    bool uniformCellWidths) {
  self->setUniformCellWidths(uniformCellWidths);
}

//  bool QQuickGridLayout::uniformCellHeights() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickGridLayout18uniformCellHeightsEv(
    const QQuickGridLayout *self) {
  return self->uniformCellHeights();
}

//  void QQuickGridLayout::setUniformCellHeights(bool uniformCellHeights)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout21setUniformCellHeightsEb(
    QQuickGridLayout *self,
    bool uniformCellHeights) {
  self->setUniformCellHeights(uniformCellHeights);
}

//  void QQuickGridLayout::insertLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout17insertLayoutItemsEv(
    QQuickGridLayout *self) {
  self->insertLayoutItems();
}

//  void QQuickGridLayout::columnSpacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout20columnSpacingChangedEv(
    QQuickGridLayout *self) {
  self->columnSpacingChanged();
}

//  void QQuickGridLayout::rowSpacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout17rowSpacingChangedEv(
    QQuickGridLayout *self) {
  self->rowSpacingChanged();
}

//  void QQuickGridLayout::columnsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout14columnsChangedEv(QQuickGridLayout *self) {
  self->columnsChanged();
}

//  void QQuickGridLayout::rowsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout11rowsChangedEv(QQuickGridLayout *self) {
  self->rowsChanged();
}

//  void QQuickGridLayout::flowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout11flowChangedEv(QQuickGridLayout *self) {
  self->flowChanged();
}

//  void QQuickGridLayout::uniformCellWidthsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout24uniformCellWidthsChangedEv(
    QQuickGridLayout *self) {
  self->uniformCellWidthsChanged();
}

//  void QQuickGridLayout::uniformCellHeightsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickGridLayout25uniformCellHeightsChangedEv(
    QQuickGridLayout *self) {
  self->uniformCellHeightsChanged();
}

//  QQuickGridLayoutPrivate *QQuickGridLayout::d_func()
extern "C" Q_DECL_EXPORT
QQuickGridLayoutPrivate *ritual_ZN16QQuickGridLayout6d_funcEv(
    QQuickGridLayout *self) {
  return self->d_func();
}

//  const QQuickGridLayoutPrivate *QQuickGridLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickGridLayoutPrivate *ritual_ZNK16QQuickGridLayout6d_funcEv(
    const QQuickGridLayout *self) {
  return self->d_func();
}

//  void QQuickGridLayout::insertLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickGridLayout17insertLayoutItemsEv(
    QQuickGridLayout *self) {
  self->QQuickGridLayout::insertLayoutItems();
}
