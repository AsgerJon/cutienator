//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextdocument.h>
#include <cstring>

//  A QAbstractUndoItem that Python can take functions over in. Every QAbstractUndoItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractUndoItemCall0)(const void *, int *);
typedef void (*CuteQAbstractUndoItemCall1)(const void *, int *);
class CuteQAbstractUndoItem : public QAbstractUndoItem {
public:
  using QAbstractUndoItem::QAbstractUndoItem;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QAbstractUndoItem4undoEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractUndoItem4redoEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractUndoItem::undo()
  void undo() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractUndoItemCall0 call = reinterpret_cast<CuteQAbstractUndoItemCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractUndoItem::redo()
  void redo() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractUndoItemCall1 call = reinterpret_cast<CuteQAbstractUndoItemCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QAbstractUndoItem::~QAbstractUndoItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractUndoItemD1Ev(QAbstractUndoItem *self) {
  delete self;
}

//  void QAbstractUndoItem::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractUndoItem4undoEv(QAbstractUndoItem *self) {
  self->undo();
}

//  void QAbstractUndoItem::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractUndoItem4redoEv(QAbstractUndoItem *self) {
  self->redo();
}

//  a Python function taken by a CuteQAbstractUndoItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractUndoItem(
    QAbstractUndoItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractUndoItem *>(self)->take(key, call);
}
