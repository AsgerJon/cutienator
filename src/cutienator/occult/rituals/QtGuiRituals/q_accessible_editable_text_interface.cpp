//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleEditableTextInterface that Python can take functions over in. Every QAccessibleEditableTextInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleEditableTextInterfaceCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleEditableTextInterfaceCall1)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleEditableTextInterfaceCall2)(const void *, int, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleEditableTextInterface : public QAccessibleEditableTextInterface {
public:
  using QAccessibleEditableTextInterface::QAccessibleEditableTextInterface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
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
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleEditableTextInterface::insertText(int offset, const
  //      QString &text)
  void insertText(int offset, const QString &text) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleEditableTextInterfaceCall1 call = reinterpret_cast<CuteQAccessibleEditableTextInterfaceCall1>(taken[1]);
      call(this, offset, &text, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleEditableTextInterface::replaceText(int startOffset,
  //      int endOffset, const QString &text)
  void replaceText(
      int startOffset,
      int endOffset,
      const QString &text) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleEditableTextInterfaceCall2 call = reinterpret_cast<CuteQAccessibleEditableTextInterfaceCall2>(taken[2]);
      call(this, startOffset, endOffset, &text, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleEditableTextInterface::QAccessibleEditableTextInterface()
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_ZN32QAccessibleEditableTextInterfaceC1Ev() {
  return new CuteQAccessibleEditableTextInterface();
}

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

#endif  // QT_CONFIG(accessibility)
