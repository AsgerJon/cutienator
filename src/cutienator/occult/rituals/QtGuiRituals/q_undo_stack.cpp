//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qundostack.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qundostack.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QUndoStack::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QUndoStack10metaObjectEv(
    const QUndoStack *self) {
  return self->metaObject();
}

//  QString QUndoStack::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QUndoStack2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUndoStack::tr(s, c, n));
}

//  QUndoStack::QUndoStack(QObject *parent)
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZN10QUndoStackC1EP7QObject(QObject *parent) {
  return new QUndoStack(parent);
}

//  QUndoStack::~QUndoStack()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStackD1Ev(QUndoStack *self) {
  delete self;
}

//  void QUndoStack::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack5clearEv(QUndoStack *self) {
  self->clear();
}

//  void QUndoStack::push(QUndoCommand *cmd)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack4pushEP12QUndoCommand(
    QUndoStack *self,
    QUndoCommand *cmd) {
  self->push(cmd);
}

//  bool QUndoStack::canUndo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack7canUndoEv(const QUndoStack *self) {
  return self->canUndo();
}

//  bool QUndoStack::canRedo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack7canRedoEv(const QUndoStack *self) {
  return self->canRedo();
}

//  QString QUndoStack::undoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoStack8undoTextEv(const QUndoStack *self) {
  return new QString(self->undoText());
}

//  QString QUndoStack::redoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoStack8redoTextEv(const QUndoStack *self) {
  return new QString(self->redoText());
}

//  int QUndoStack::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack5countEv(const QUndoStack *self) {
  return self->count();
}

//  int QUndoStack::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack5indexEv(const QUndoStack *self) {
  return self->index();
}

//  QString QUndoStack::text(int idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoStack4textEi(const QUndoStack *self, int idx) {
  return new QString(self->text(idx));
}

//  QAction *QUndoStack::createUndoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoStack16createUndoActionEP7QObjectRK7QString(
    const QUndoStack *self,
    QObject *parent,
    const QString *prefix) {
  return self->createUndoAction(parent, *prefix);
}

//  QAction *QUndoStack::createRedoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoStack16createRedoActionEP7QObjectRK7QString(
    const QUndoStack *self,
    QObject *parent,
    const QString *prefix) {
  return self->createRedoAction(parent, *prefix);
}

//  bool QUndoStack::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack8isActiveEv(const QUndoStack *self) {
  return self->isActive();
}

//  bool QUndoStack::isClean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack7isCleanEv(const QUndoStack *self) {
  return self->isClean();
}

//  int QUndoStack::cleanIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack10cleanIndexEv(const QUndoStack *self) {
  return self->cleanIndex();
}

//  void QUndoStack::beginMacro(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack10beginMacroERK7QString(
    QUndoStack *self,
    const QString *text) {
  self->beginMacro(*text);
}

//  void QUndoStack::endMacro()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack8endMacroEv(QUndoStack *self) {
  self->endMacro();
}

//  void QUndoStack::setUndoLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack12setUndoLimitEi(QUndoStack *self, int limit) {
  self->setUndoLimit(limit);
}

//  int QUndoStack::undoLimit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack9undoLimitEv(const QUndoStack *self) {
  return self->undoLimit();
}

//  const QUndoCommand *QUndoStack::command(int index) const
extern "C" Q_DECL_EXPORT
const QUndoCommand *ritual_ZNK10QUndoStack7commandEi(
    const QUndoStack *self,
    int index) {
  return self->command(index);
}

//  void QUndoStack::setClean()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack8setCleanEv(QUndoStack *self) {
  self->setClean();
}

//  void QUndoStack::resetClean()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack10resetCleanEv(QUndoStack *self) {
  self->resetClean();
}

//  void QUndoStack::setIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack8setIndexEi(QUndoStack *self, int idx) {
  self->setIndex(idx);
}

//  void QUndoStack::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack4undoEv(QUndoStack *self) {
  self->undo();
}

//  void QUndoStack::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack4redoEv(QUndoStack *self) {
  self->redo();
}

//  void QUndoStack::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack9setActiveEb(QUndoStack *self, bool active) {
  self->setActive(active);
}
