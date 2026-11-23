//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QTextObjectInterface that Python can take functions over in. Every QTextObjectInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSizeF * (*CuteQTextObjectInterfaceCall0)(const void *, QTextDocument *, int, const QTextFormat *, int *);
typedef void (*CuteQTextObjectInterfaceCall1)(const void *, QPainter *, const QRectF *, QTextDocument *, int, const QTextFormat *, int *);
class CuteQTextObjectInterface : public QTextObjectInterface {
public:
  using QTextObjectInterface::QTextObjectInterface;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QTextObjectInterface13intrinsicSizeEP13QTextDocumentiRK11QTextFormat")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QTextObjectInterface10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QSizeF QTextObjectInterface::intrinsicSize(QTextDocument *doc, int
  //      posInDocument, const QTextFormat &format)
  QSizeF intrinsicSize(
      QTextDocument *doc,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextObjectInterfaceCall0 call = reinterpret_cast<CuteQTextObjectInterfaceCall0>(taken[0]);
      const QSizeF * given = call(this, doc, posInDocument, &format, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QTextObjectInterface::drawObject(QPainter *painter, const QRectF
  //      &rect, QTextDocument *doc, int posInDocument, const QTextFormat
  //      &format)
  void drawObject(
      QPainter *painter,
      const QRectF &rect,
      QTextDocument *doc,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextObjectInterfaceCall1 call = reinterpret_cast<CuteQTextObjectInterfaceCall1>(taken[1]);
      call(this, painter, &rect, doc, posInDocument, &format, &handled);
      if (handled) return;
    }
  }
};

//  QTextObjectInterface::~QTextObjectInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextObjectInterfaceD1Ev(QTextObjectInterface *self) {
  delete self;
}

//  QSizeF QTextObjectInterface::intrinsicSize(QTextDocument *doc, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN20QTextObjectInterface13intrinsicSizeEP13QTextDocumentiRK11QTextFormat(
    QTextObjectInterface *self,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  return new QSizeF(self->intrinsicSize(doc, posInDocument, *format));
}

//  void QTextObjectInterface::drawObject(QPainter *painter, const QRectF
//      &rect, QTextDocument *doc, int posInDocument, const QTextFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextObjectInterface10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat(
    QTextObjectInterface *self,
    QPainter *painter,
    const QRectF *rect,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  self->drawObject(painter, *rect, doc, posInDocument, *format);
}

//  a Python function taken by a CuteQTextObjectInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextObjectInterface(
    QTextObjectInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextObjectInterface *>(self)->take(key, call);
}
