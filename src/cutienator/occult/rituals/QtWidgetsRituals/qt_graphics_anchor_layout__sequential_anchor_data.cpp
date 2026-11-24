//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QtGraphicsAnchorLayout::SequentialAnchorData that Python can take functions over in. Every QtGraphicsAnchorLayout::SequentialAnchorData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQtGraphicsAnchorLayout_SequentialAnchorDataCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQtGraphicsAnchorLayout_SequentialAnchorData : public QtGraphicsAnchorLayout::SequentialAnchorData {
public:
  using QtGraphicsAnchorLayout::SequentialAnchorData::SequentialAnchorData;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildrenSizesEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void
  //      QtGraphicsAnchorLayout::SequentialAnchorData::updateChildrenSizes
  //      ()
  void updateChildrenSizes() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtGraphicsAnchorLayout_SequentialAnchorDataCall0 call = reinterpret_cast<CuteQtGraphicsAnchorLayout_SequentialAnchorDataCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtGraphicsAnchorLayout::SequentialAnchorData::updateChildrenSizes();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  void QtGraphicsAnchorLayout::SequentialAnchorData::updateChildrenSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtGraphicsAnchorLayout20SequentialAnchorData19updateChildrenSizesEv(
    QtGraphicsAnchorLayout::SequentialAnchorData *self) {
  self->updateChildrenSizes();
}

//  a Python function taken by a
//      CuteQtGraphicsAnchorLayout_SequentialAnchorData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtGraphicsAnchorLayout_SequentialAnchorData(
    QtGraphicsAnchorLayout::SequentialAnchorData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtGraphicsAnchorLayout_SequentialAnchorData *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
