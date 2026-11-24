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

//  A QtGraphicsAnchorLayout::ParallelAnchorData that Python can take functions over in. Every QtGraphicsAnchorLayout::ParallelAnchorData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQtGraphicsAnchorLayout_ParallelAnchorDataCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQtGraphicsAnchorLayout_ParallelAnchorData : public QtGraphicsAnchorLayout::ParallelAnchorData {
public:
  using QtGraphicsAnchorLayout::ParallelAnchorData::ParallelAnchorData;
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
  //      QtGraphicsAnchorLayout::ParallelAnchorData::updateChildrenSizes()
  void updateChildrenSizes() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtGraphicsAnchorLayout_ParallelAnchorDataCall0 call = reinterpret_cast<CuteQtGraphicsAnchorLayout_ParallelAnchorDataCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtGraphicsAnchorLayout::ParallelAnchorData::updateChildrenSizes();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  void QtGraphicsAnchorLayout::ParallelAnchorData::updateChildrenSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtGraphicsAnchorLayout18ParallelAnchorData19updateChildrenSizesEv(
    QtGraphicsAnchorLayout::ParallelAnchorData *self) {
  self->updateChildrenSizes();
}

//  bool QtGraphicsAnchorLayout::ParallelAnchorData::secondForward() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QtGraphicsAnchorLayout18ParallelAnchorData13secondForwardEv(
    const QtGraphicsAnchorLayout::ParallelAnchorData *self) {
  return self->secondForward();
}

//  a Python function taken by a
//      CuteQtGraphicsAnchorLayout_ParallelAnchorData, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtGraphicsAnchorLayout_ParallelAnchorData(
    QtGraphicsAnchorLayout::ParallelAnchorData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtGraphicsAnchorLayout_ParallelAnchorData *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
