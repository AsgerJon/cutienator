//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMetalCommandBuffer that Python can take functions over in. Every QMetalCommandBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalCommandBufferCall0)(const void *, int *);
typedef int (*CuteQMetalCommandBufferCall1)(const void *, int *);
class CuteQMetalCommandBuffer : public QMetalCommandBuffer {
public:
  using QMetalCommandBuffer::QMetalCommandBuffer;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QMetalCommandBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalCommandBufferCall0 call = reinterpret_cast<CuteQMetalCommandBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalCommandBuffer::destroy();
  }

  //  QRhiResource::Type QRhiCommandBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalCommandBufferCall1 call = reinterpret_cast<CuteQMetalCommandBufferCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiCommandBuffer::resourceType();
  }
};

//  a Python function taken by a CuteQMetalCommandBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalCommandBuffer(
    QMetalCommandBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalCommandBuffer *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
