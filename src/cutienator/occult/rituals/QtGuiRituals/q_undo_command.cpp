//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qundostack.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(undocommand)
#include <QtGui/qundostack.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QUndoCommand that Python can take functions over in. Every QUndoCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*CuteQUndoCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*CuteQUndoCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*CuteQUndoCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*CuteQUndoCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class CuteQUndoCommand : public QUndoCommand {
public:
  using QUndoCommand::QUndoCommand;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4undoEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4redoEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZNK12QUndoCommand2idEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand9mergeWithEPKS_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
    return false;
  }

#if QT_CONFIG(undocommand)
  //  void QUndoCommand::undo()
  void undo() override {
    if (taken[0]) {
      int handled = 0;
      CuteQUndoCommandCall0 call = reinterpret_cast<CuteQUndoCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QUndoCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void QUndoCommand::redo()
  void redo() override {
    if (taken[1]) {
      int handled = 0;
      CuteQUndoCommandCall1 call = reinterpret_cast<CuteQUndoCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QUndoCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQUndoCommandCall2 call = reinterpret_cast<CuteQUndoCommandCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUndoCommand::id();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  bool QUndoCommand::mergeWith(const QUndoCommand *other)
  bool mergeWith(const QUndoCommand *other) override {
    if (taken[3]) {
      int handled = 0;
      CuteQUndoCommandCall3 call = reinterpret_cast<CuteQUndoCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  QUndoCommand::QUndoCommand(QUndoCommand *parent)
extern "C" Q_DECL_EXPORT
QUndoCommand *ritual_ZN12QUndoCommandC1EPS_(QUndoCommand *parent) {
  return new CuteQUndoCommand(parent);
}

//  QUndoCommand::QUndoCommand(const QString &text, QUndoCommand *parent)
extern "C" Q_DECL_EXPORT
QUndoCommand *ritual_ZN12QUndoCommandC1ERK7QStringPS_(
    const QString *text,
    QUndoCommand *parent) {
  return new CuteQUndoCommand(*text, parent);
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

//  a Python function taken by a CuteQUndoCommand, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUndoCommand(
    QUndoCommand *self,
    const char *key,
    void *call) {
  return static_cast<CuteQUndoCommand *>(self)->take(key, call);
}

//  void QUndoCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QUndoCommand4undoEv(QUndoCommand *self) {
  self->QUndoCommand::undo();
}

//  void QUndoCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QUndoCommand4redoEv(QUndoCommand *self) {
  self->QUndoCommand::redo();
}

//  int QUndoCommand::id() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QUndoCommand2idEv(const QUndoCommand *self) {
  return self->QUndoCommand::id();
}

//  bool QUndoCommand::mergeWith(const QUndoCommand *other)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QUndoCommand9mergeWithEPKS_(
    QUndoCommand *self,
    const QUndoCommand *other) {
  return self->QUndoCommand::mergeWith(other);
}

#endif  // QT_CONFIG(undocommand)
