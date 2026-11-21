//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qundogroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qundogroup.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QUndoGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QUndoGroup10metaObjectEv(
    const QUndoGroup *self) {
  return self->metaObject();
}

//  QString QUndoGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QUndoGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUndoGroup::tr(s, c, n));
}

//  QUndoGroup::QUndoGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QUndoGroup *ritual_ZN10QUndoGroupC1EP7QObject(QObject *parent) {
  return new QUndoGroup(parent);
}

//  QUndoGroup::~QUndoGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroupD1Ev(QUndoGroup *self) {
  delete self;
}

//  void QUndoGroup::addStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup8addStackEP10QUndoStack(
    QUndoGroup *self,
    QUndoStack *stack) {
  self->addStack(stack);
}

//  void QUndoGroup::removeStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup11removeStackEP10QUndoStack(
    QUndoGroup *self,
    QUndoStack *stack) {
  self->removeStack(stack);
}

//  QUndoStack *QUndoGroup::activeStack() const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZNK10QUndoGroup11activeStackEv(const QUndoGroup *self) {
  return self->activeStack();
}

//  QAction *QUndoGroup::createUndoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoGroup16createUndoActionEP7QObjectRK7QString(
    const QUndoGroup *self,
    QObject *parent,
    const QString *prefix) {
  return self->createUndoAction(parent, *prefix);
}

//  QAction *QUndoGroup::createRedoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoGroup16createRedoActionEP7QObjectRK7QString(
    const QUndoGroup *self,
    QObject *parent,
    const QString *prefix) {
  return self->createRedoAction(parent, *prefix);
}

//  bool QUndoGroup::canUndo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoGroup7canUndoEv(const QUndoGroup *self) {
  return self->canUndo();
}

//  bool QUndoGroup::canRedo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoGroup7canRedoEv(const QUndoGroup *self) {
  return self->canRedo();
}

//  QString QUndoGroup::undoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoGroup8undoTextEv(const QUndoGroup *self) {
  return new QString(self->undoText());
}

//  QString QUndoGroup::redoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoGroup8redoTextEv(const QUndoGroup *self) {
  return new QString(self->redoText());
}

//  bool QUndoGroup::isClean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoGroup7isCleanEv(const QUndoGroup *self) {
  return self->isClean();
}

//  void QUndoGroup::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup4undoEv(QUndoGroup *self) {
  self->undo();
}

//  void QUndoGroup::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup4redoEv(QUndoGroup *self) {
  self->redo();
}

//  void QUndoGroup::setActiveStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup14setActiveStackEP10QUndoStack(
    QUndoGroup *self,
    QUndoStack *stack) {
  self->setActiveStack(stack);
}
