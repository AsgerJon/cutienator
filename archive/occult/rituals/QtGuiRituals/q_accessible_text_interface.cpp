//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QAccessibleTextInterface that Python can take functions over in. Every QAccessibleTextInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAccessibleTextInterfaceCall0)(const void *, int *);
typedef void (*CuteQAccessibleTextInterfaceCall1)(const void *, int, int, int *);
typedef void (*CuteQAccessibleTextInterfaceCall2)(const void *, int, int *);
typedef void (*CuteQAccessibleTextInterfaceCall3)(const void *, int, int, int, int *);
typedef int (*CuteQAccessibleTextInterfaceCall4)(const void *, int *);
typedef void (*CuteQAccessibleTextInterfaceCall5)(const void *, int, int *);
typedef QString * (*CuteQAccessibleTextInterfaceCall6)(const void *, int, int, int *);
typedef int (*CuteQAccessibleTextInterfaceCall7)(const void *, int *);
typedef const QRect * (*CuteQAccessibleTextInterfaceCall8)(const void *, int, int *);
typedef int (*CuteQAccessibleTextInterfaceCall9)(const void *, const QPoint *, int *);
typedef void (*CuteQAccessibleTextInterfaceCall10)(const void *, int, int, int *);
class CuteQAccessibleTextInterface : public QAccessibleTextInterface {
public:
  using QAccessibleTextInterface::QAccessibleTextInterface;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  int QAccessibleTextInterface::selectionCount() const
  int selectionCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall0 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAccessibleTextInterface::addSelection(int startOffset, int
  //      endOffset)
  void addSelection(int startOffset, int endOffset) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall1 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall1>(taken[1]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
  }

  //  void QAccessibleTextInterface::removeSelection(int selectionIndex)
  void removeSelection(int selectionIndex) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall2 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall2>(taken[2]);
      call(this, selectionIndex, &handled);
      if (handled) return;
    }
  }

  //  void QAccessibleTextInterface::setSelection(int selectionIndex, int
  //      startOffset, int endOffset)
  void setSelection(
      int selectionIndex,
      int startOffset,
      int endOffset) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall3 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall3>(taken[3]);
      call(this, selectionIndex, startOffset, endOffset, &handled);
      if (handled) return;
    }
  }

  //  int QAccessibleTextInterface::cursorPosition() const
  int cursorPosition() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall4 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAccessibleTextInterface::setCursorPosition(int position)
  void setCursorPosition(int position) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall5 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall5>(taken[5]);
      call(this, position, &handled);
      if (handled) return;
    }
  }

  //  QString QAccessibleTextInterface::text(int startOffset, int
  //      endOffset) const
  QString text(int startOffset, int endOffset) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall6 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall6>(taken[6]);
      QString * given = call(this, startOffset, endOffset, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QAccessibleTextInterface::characterCount() const
  int characterCount() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall7 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRect QAccessibleTextInterface::characterRect(int offset) const
  QRect characterRect(int offset) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall8 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall8>(taken[8]);
      const QRect * given = call(this, offset, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QAccessibleTextInterface::offsetAtPoint(const QPoint &point)
  //      const
  int offsetAtPoint(const QPoint &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall9 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall9>(taken[9]);
      int given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAccessibleTextInterface::scrollToSubstring(int startIndex, int
  //      endIndex)
  void scrollToSubstring(int startIndex, int endIndex) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleTextInterfaceCall10 call = reinterpret_cast<CuteQAccessibleTextInterfaceCall10>(taken[10]);
      call(this, startIndex, endIndex, &handled);
      if (handled) return;
    }
  }
};

//  QAccessibleTextInterface::~QAccessibleTextInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterfaceD1Ev(
    QAccessibleTextInterface *self) {
  delete self;
}

//  void QAccessibleTextInterface::selection(int selectionIndex, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAccessibleTextInterface9selectionEiPiS0_(
    const QAccessibleTextInterface *self,
    int selectionIndex,
    int *startOffset,
    int *endOffset) {
  self->selection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleTextInterface::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface14selectionCountEv(
    const QAccessibleTextInterface *self) {
  return self->selectionCount();
}

//  void QAccessibleTextInterface::addSelection(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface12addSelectionEii(
    QAccessibleTextInterface *self,
    int startOffset,
    int endOffset) {
  self->addSelection(startOffset, endOffset);
}

//  void QAccessibleTextInterface::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface15removeSelectionEi(
    QAccessibleTextInterface *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleTextInterface::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface12setSelectionEiii(
    QAccessibleTextInterface *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleTextInterface::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface14cursorPositionEv(
    const QAccessibleTextInterface *self) {
  return self->cursorPosition();
}

//  void QAccessibleTextInterface::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface17setCursorPositionEi(
    QAccessibleTextInterface *self,
    int position) {
  self->setCursorPosition(position);
}

//  QString QAccessibleTextInterface::text(int startOffset, int endOffset)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface4textEii(
    const QAccessibleTextInterface *self,
    int startOffset,
    int endOffset) {
  return new QString(self->text(startOffset, endOffset));
}

//  QString QAccessibleTextInterface::textBeforeOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextInterface *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textBeforeOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleTextInterface::textAfterOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextInterface *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAfterOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleTextInterface::textAtOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextInterface *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAtOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  int QAccessibleTextInterface::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface14characterCountEv(
    const QAccessibleTextInterface *self) {
  return self->characterCount();
}

//  QRect QAccessibleTextInterface::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24QAccessibleTextInterface13characterRectEi(
    const QAccessibleTextInterface *self,
    int offset) {
  return new QRect(self->characterRect(offset));
}

//  int QAccessibleTextInterface::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint(
    const QAccessibleTextInterface *self,
    const QPoint *point) {
  return self->offsetAtPoint(*point);
}

//  void QAccessibleTextInterface::scrollToSubstring(int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface17scrollToSubstringEii(
    QAccessibleTextInterface *self,
    int startIndex,
    int endIndex) {
  self->scrollToSubstring(startIndex, endIndex);
}

//  QString QAccessibleTextInterface::attributes(int offset, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface10attributesEiPiS0_(
    const QAccessibleTextInterface *self,
    int offset,
    int *startOffset,
    int *endOffset) {
  return new QString(self->attributes(offset, startOffset, endOffset));
}

//  a Python function taken by a CuteQAccessibleTextInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextInterface(
    QAccessibleTextInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextInterface *>(self)->take(key, call);
}
