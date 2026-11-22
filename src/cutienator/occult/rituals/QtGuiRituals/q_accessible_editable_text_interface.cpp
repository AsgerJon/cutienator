//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleEditableTextInterface that Python can take functions over in. Every QAccessibleEditableTextInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAccessibleEditableTextInterfaceCall0)(const void *, int, int, int *);
class CuteQAccessibleEditableTextInterface : public QAccessibleEditableTextInterface {
public:
  using QAccessibleEditableTextInterface::QAccessibleEditableTextInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QAccessibleEditableTextInterface::deleteText(int startOffset,
  //      int endOffset)
  void deleteText(int startOffset, int endOffset) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleEditableTextInterfaceCall0 call = reinterpret_cast<CuteQAccessibleEditableTextInterfaceCall0>(taken[0]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
  }
};

//  QAccessibleEditableTextInterface::~QAccessibleEditableTextInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterfaceD1Ev(
    QAccessibleEditableTextInterface *self) {
  delete self;
}

//  void QAccessibleEditableTextInterface::deleteText(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterface10deleteTextEii(
    QAccessibleEditableTextInterface *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleEditableTextInterface::insertText(int offset, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString(
    QAccessibleEditableTextInterface *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleEditableTextInterface::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString(
    QAccessibleEditableTextInterface *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}

//  a Python function taken by a CuteQAccessibleEditableTextInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleEditableTextInterface(
    QAccessibleEditableTextInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleEditableTextInterface *>(self)->take(key, call);
}
