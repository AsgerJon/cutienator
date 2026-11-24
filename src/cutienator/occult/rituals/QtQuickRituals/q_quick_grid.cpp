//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickGrid may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGrid : QQuickGrid {
  using QQuickGrid::doPositioning;
  using QQuickGrid::reportConflictingAnchors;
};

//  const QMetaObject *QQuickGrid::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickGrid10metaObjectEv(
    const QQuickGrid *self) {
  return self->metaObject();
}

//  QString QQuickGrid::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickGrid2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGrid::tr(s, c, n));
}

//  QQuickGrid::QQuickGrid(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGrid *ritual_ZN10QQuickGridC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickGrid(parent);
}

//  int QQuickGrid::rows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickGrid4rowsEv(const QQuickGrid *self) {
  return self->rows();
}

//  void QQuickGrid::setRows(const int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid7setRowsEi(QQuickGrid *self, int rows) {
  self->setRows(rows);
}

//  int QQuickGrid::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickGrid7columnsEv(const QQuickGrid *self) {
  return self->columns();
}

//  void QQuickGrid::setColumns(const int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid10setColumnsEi(QQuickGrid *self, int columns) {
  self->setColumns(columns);
}

//  qreal QQuickGrid::rowSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickGrid10rowSpacingEv(const QQuickGrid *self) {
  return self->rowSpacing();
}

//  void QQuickGrid::setRowSpacing(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid13setRowSpacingEd(QQuickGrid *self, qreal a0) {
  self->setRowSpacing(a0);
}

//  void QQuickGrid::resetRowSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid15resetRowSpacingEv(QQuickGrid *self) {
  self->resetRowSpacing();
}

//  qreal QQuickGrid::columnSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickGrid13columnSpacingEv(const QQuickGrid *self) {
  return self->columnSpacing();
}

//  void QQuickGrid::setColumnSpacing(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid16setColumnSpacingEd(QQuickGrid *self, qreal a0) {
  self->setColumnSpacing(a0);
}

//  void QQuickGrid::resetColumnSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid18resetColumnSpacingEv(QQuickGrid *self) {
  self->resetColumnSpacing();
}

//  Flow QQuickGrid::flow() const
extern "C" Q_DECL_EXPORT
QQuickGrid::Flow ritual_ZNK10QQuickGrid4flowEv(const QQuickGrid *self) {
  return self->flow();
}

//  void QQuickGrid::setFlow(Flow a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid7setFlowENS_4FlowE(
    QQuickGrid *self,
    QQuickGrid::Flow a0) {
  self->setFlow(a0);
}

//  Qt::LayoutDirection QQuickGrid::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK10QQuickGrid15layoutDirectionEv(
    const QQuickGrid *self) {
  return self->layoutDirection();
}

//  void QQuickGrid::setLayoutDirection(Qt::LayoutDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QQuickGrid *self,
    Qt::LayoutDirection a0) {
  self->setLayoutDirection(a0);
}

//  Qt::LayoutDirection QQuickGrid::effectiveLayoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK10QQuickGrid24effectiveLayoutDirectionEv(
    const QQuickGrid *self) {
  return self->effectiveLayoutDirection();
}

//  HAlignment QQuickGrid::hItemAlign() const
extern "C" Q_DECL_EXPORT
QQuickGrid::HAlignment ritual_ZNK10QQuickGrid10hItemAlignEv(
    const QQuickGrid *self) {
  return self->hItemAlign();
}

//  void QQuickGrid::setHItemAlign(HAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid13setHItemAlignENS_10HAlignmentE(
    QQuickGrid *self,
    QQuickGrid::HAlignment align) {
  self->setHItemAlign(align);
}

//  HAlignment QQuickGrid::effectiveHAlign() const
extern "C" Q_DECL_EXPORT
QQuickGrid::HAlignment ritual_ZNK10QQuickGrid15effectiveHAlignEv(
    const QQuickGrid *self) {
  return self->effectiveHAlign();
}

//  VAlignment QQuickGrid::vItemAlign() const
extern "C" Q_DECL_EXPORT
QQuickGrid::VAlignment ritual_ZNK10QQuickGrid10vItemAlignEv(
    const QQuickGrid *self) {
  return self->vItemAlign();
}

//  void QQuickGrid::setVItemAlign(VAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid13setVItemAlignENS_10VAlignmentE(
    QQuickGrid *self,
    QQuickGrid::VAlignment align) {
  self->setVItemAlign(align);
}

//  void QQuickGrid::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid13doPositioningEP6QSizeF(
    QQuickGrid *self,
    QSizeF *contentSize) {
  self->doPositioning(contentSize);
}

//  void QQuickGrid::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickGrid24reportConflictingAnchorsEv(QQuickGrid *self) {
  self->reportConflictingAnchors();
}

//  void QQuickGrid::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickGrid13doPositioningEP6QSizeF(
    QQuickGrid *self,
    QSizeF *contentSize) {
  static_cast<OwnQQuickGrid *>(self)->OwnQQuickGrid::doPositioning(
      contentSize);
}

//  void QQuickGrid::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickGrid24reportConflictingAnchorsEv(
    QQuickGrid *self) {
  static_cast<OwnQQuickGrid *>(self)->OwnQQuickGrid::reportConflictingAnchors();
}

#endif  // QT_CONFIG(quick_positioners)
