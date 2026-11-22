//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qundostack.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qundostack.h>
#include <QtCore/qstring.h>

//  QUndoCommand::QUndoCommand(QUndoCommand *parent)
extern "C" Q_DECL_EXPORT
QUndoCommand *ritual_ZN12QUndoCommandC1EPS_(QUndoCommand *parent) {
  return new QUndoCommand(parent);
}

//  QUndoCommand::QUndoCommand(const QString &text, QUndoCommand *parent)
extern "C" Q_DECL_EXPORT
QUndoCommand *ritual_ZN12QUndoCommandC1ERK7QStringPS_(
    const QString *text,
    QUndoCommand *parent) {
  return new QUndoCommand(*text, parent);
}

//  QUndoCommand::~QUndoCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QUndoCommandD1Ev(QUndoCommand *self) {
  delete self;
}

//  void QUndoCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QUndoCommand4undoEv(QUndoCommand *self) {
  self->undo();
}

//  void QUndoCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QUndoCommand4redoEv(QUndoCommand *self) {
  self->redo();
}

//  QString QUndoCommand::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QUndoCommand4textEv(const QUndoCommand *self) {
  return new QString(self->text());
}

//  QString QUndoCommand::actionText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QUndoCommand10actionTextEv(const QUndoCommand *self) {
  return new QString(self->actionText());
}

//  void QUndoCommand::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QUndoCommand7setTextERK7QString(
    QUndoCommand *self,
    const QString *text) {
  self->setText(*text);
}

//  bool QUndoCommand::isObsolete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QUndoCommand10isObsoleteEv(const QUndoCommand *self) {
  return self->isObsolete();
}

//  void QUndoCommand::setObsolete(bool obsolete)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QUndoCommand11setObsoleteEb(
    QUndoCommand *self,
    bool obsolete) {
  self->setObsolete(obsolete);
}

//  int QUndoCommand::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QUndoCommand2idEv(const QUndoCommand *self) {
  return self->id();
}

//  bool QUndoCommand::mergeWith(const QUndoCommand *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QUndoCommand9mergeWithEPKS_(
    QUndoCommand *self,
    const QUndoCommand *other) {
  return self->mergeWith(other);
}

//  int QUndoCommand::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QUndoCommand10childCountEv(const QUndoCommand *self) {
  return self->childCount();
}

//  const QUndoCommand *QUndoCommand::child(int index) const
extern "C" Q_DECL_EXPORT
const QUndoCommand *ritual_ZNK12QUndoCommand5childEi(
    const QUndoCommand *self,
    int index) {
  return self->child(index);
}
