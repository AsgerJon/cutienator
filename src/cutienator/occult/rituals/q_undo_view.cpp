//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qundoview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qundoview.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *QUndoView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QUndoView10metaObjectEv(
    const QUndoView *self) {
  return self->metaObject();
}

//  QString QUndoView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QUndoView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUndoView::tr(s, c, n));
}

//  QUndoView::QUndoView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QUndoView *ritual_ZN9QUndoViewC1EP7QWidget(QWidget *parent) {
  return new QUndoView(parent);
}

//  QUndoView::QUndoView(QUndoStack *stack, QWidget *parent)
extern "C" Q_DECL_EXPORT
QUndoView *ritual_ZN9QUndoViewC1EP10QUndoStackP7QWidget(
    QUndoStack *stack,
    QWidget *parent) {
  return new QUndoView(stack, parent);
}

//  QUndoView::QUndoView(QUndoGroup *group, QWidget *parent)
extern "C" Q_DECL_EXPORT
QUndoView *ritual_ZN9QUndoViewC1EP10QUndoGroupP7QWidget(
    QUndoGroup *group,
    QWidget *parent) {
  return new QUndoView(group, parent);
}

//  QUndoView::~QUndoView()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoViewD1Ev(QUndoView *self) {
  delete self;
}

//  QUndoStack *QUndoView::stack() const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZNK9QUndoView5stackEv(const QUndoView *self) {
  return self->stack();
}

//  QUndoGroup *QUndoView::group() const
extern "C" Q_DECL_EXPORT
QUndoGroup *ritual_ZNK9QUndoView5groupEv(const QUndoView *self) {
  return self->group();
}

//  void QUndoView::setEmptyLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView13setEmptyLabelERK7QString(
    QUndoView *self,
    const QString *label) {
  self->setEmptyLabel(*label);
}

//  QString QUndoView::emptyLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QUndoView10emptyLabelEv(const QUndoView *self) {
  return new QString(self->emptyLabel());
}

//  void QUndoView::setCleanIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView12setCleanIconERK5QIcon(
    QUndoView *self,
    const QIcon *icon) {
  self->setCleanIcon(*icon);
}

//  QIcon QUndoView::cleanIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK9QUndoView9cleanIconEv(const QUndoView *self) {
  return new QIcon(self->cleanIcon());
}

//  void QUndoView::setStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView8setStackEP10QUndoStack(
    QUndoView *self,
    QUndoStack *stack) {
  self->setStack(stack);
}

//  void QUndoView::setGroup(QUndoGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView8setGroupEP10QUndoGroup(
    QUndoView *self,
    QUndoGroup *group) {
  self->setGroup(group);
}
