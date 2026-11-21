//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcolumnview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcolumnview.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QColumnView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QColumnView10metaObjectEv(
    const QColumnView *self) {
  return self->metaObject();
}

//  QString QColumnView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QColumnView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColumnView::tr(s, c, n));
}

//  QColumnView::QColumnView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QColumnView *ritual_ZN11QColumnViewC1EP7QWidget(QWidget *parent) {
  return new QColumnView(parent);
}

//  QColumnView::~QColumnView()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnViewD1Ev(QColumnView *self) {
  delete self;
}

//  QModelIndex QColumnView::indexAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QColumnView7indexAtERK6QPoint(
    const QColumnView *self,
    const QPoint *point) {
  return new QModelIndex(self->indexAt(*point));
}

//  void QColumnView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QColumnView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QSize QColumnView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QColumnView8sizeHintEv(const QColumnView *self) {
  return new QSize(self->sizeHint());
}

//  QRect QColumnView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QColumnView10visualRectERK11QModelIndex(
    const QColumnView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QColumnView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView8setModelEP18QAbstractItemModel(
    QColumnView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  void QColumnView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView17setSelectionModelEP19QItemSelectionModel(
    QColumnView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  void QColumnView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView12setRootIndexERK11QModelIndex(
    QColumnView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QColumnView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView9selectAllEv(QColumnView *self) {
  self->selectAll();
}

//  void QColumnView::setResizeGripsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView21setResizeGripsVisibleEb(
    QColumnView *self,
    bool visible) {
  self->setResizeGripsVisible(visible);
}

//  bool QColumnView::resizeGripsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColumnView18resizeGripsVisibleEv(const QColumnView *self) {
  return self->resizeGripsVisible();
}

//  void QColumnView::setPreviewColumnVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView23setPreviewColumnVisibleEb(
    QColumnView *self,
    bool visible) {
  self->setPreviewColumnVisible(visible);
}

//  bool QColumnView::isPreviewColumnVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColumnView22isPreviewColumnVisibleEv(
    const QColumnView *self) {
  return self->isPreviewColumnVisible();
}

//  QWidget *QColumnView::previewWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QColumnView13previewWidgetEv(const QColumnView *self) {
  return self->previewWidget();
}

//  void QColumnView::setPreviewWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView16setPreviewWidgetEP7QWidget(
    QColumnView *self,
    QWidget *widget) {
  self->setPreviewWidget(widget);
}
