
# This file is autogenerated by update.py

@ stdcall -version=0x600+ AcquireSRWLockExclusive() kernel32.AcquireSRWLockExclusive
@ stdcall -version=0x600+ AcquireSRWLockShared() kernel32.AcquireSRWLockShared
@ stdcall CancelWaitableTimer() kernel32.CancelWaitableTimer
@ stdcall CreateEventA() kernel32.CreateEventA
@ stdcall -version=0x600+ CreateEventExA() kernel32.CreateEventExA
@ stdcall -version=0x600+ CreateEventExW() kernel32.CreateEventExW
@ stdcall CreateEventW() kernel32.CreateEventW
@ stdcall CreateMutexA() kernel32.CreateMutexA
@ stdcall -version=0x600+ CreateMutexExA() kernel32.CreateMutexExA
@ stdcall -version=0x600+ CreateMutexExW() kernel32.CreateMutexExW
@ stdcall CreateMutexW() kernel32.CreateMutexW
@ stdcall -version=0x600+ CreateSemaphoreExW() kernel32.CreateSemaphoreExW
@ stdcall -version=0x600+ CreateWaitableTimerExW() kernel32.CreateWaitableTimerExW
@ stdcall DeleteCriticalSection() kernel32.DeleteCriticalSection
@ stub DeleteSynchronizationBarrier
@ stdcall EnterCriticalSection() kernel32.EnterCriticalSection
@ stub EnterSynchronizationBarrier
@ stdcall -version=0x600+ InitOnceBeginInitialize() kernel32.InitOnceBeginInitialize
@ stdcall -version=0x600+ InitOnceComplete() kernel32.InitOnceComplete
@ stdcall -version=0x600+ InitOnceExecuteOnce() kernel32.InitOnceExecuteOnce
@ stdcall -version=0x600+ InitOnceInitialize() kernel32.InitOnceInitialize
@ stdcall -version=0x600+ InitializeConditionVariable() kernel32.InitializeConditionVariable
@ stdcall InitializeCriticalSection() kernel32.InitializeCriticalSection
@ stdcall InitializeCriticalSectionAndSpinCount() kernel32.InitializeCriticalSectionAndSpinCount
@ stdcall -version=0x600+ InitializeCriticalSectionEx() kernel32.InitializeCriticalSectionEx
@ stdcall -version=0x600+ InitializeSRWLock() kernel32.InitializeSRWLock
@ stub InitializeSynchronizationBarrier
@ stdcall LeaveCriticalSection() kernel32.LeaveCriticalSection
@ stdcall OpenEventA() kernel32.OpenEventA
@ stdcall OpenEventW() kernel32.OpenEventW
@ stdcall OpenMutexW() kernel32.OpenMutexW
@ stdcall OpenSemaphoreW() kernel32.OpenSemaphoreW
@ stdcall OpenWaitableTimerW() kernel32.OpenWaitableTimerW
@ stdcall ReleaseMutex() kernel32.ReleaseMutex
@ stdcall -version=0x600+ ReleaseSRWLockExclusive() kernel32.ReleaseSRWLockExclusive
@ stdcall -version=0x600+ ReleaseSRWLockShared() kernel32.ReleaseSRWLockShared
@ stdcall ReleaseSemaphore() kernel32.ReleaseSemaphore
@ stdcall ResetEvent() kernel32.ResetEvent
@ stdcall SetCriticalSectionSpinCount() kernel32.SetCriticalSectionSpinCount
@ stdcall SetEvent() kernel32.SetEvent
@ stdcall SetWaitableTimer() kernel32.SetWaitableTimer
@ stub SetWaitableTimerEx
@ stdcall SignalObjectAndWait() kernel32.SignalObjectAndWait
@ stdcall Sleep() kernel32.Sleep
@ stdcall -version=0x600+ SleepConditionVariableCS() kernel32.SleepConditionVariableCS
@ stdcall -version=0x600+ SleepConditionVariableSRW() kernel32.SleepConditionVariableSRW
@ stdcall SleepEx() kernel32.SleepEx
@ stub TryAcquireSRWLockExclusive
@ stub TryAcquireSRWLockShared
@ stdcall TryEnterCriticalSection() kernel32.TryEnterCriticalSection
@ stdcall WaitForMultipleObjectsEx() kernel32.WaitForMultipleObjectsEx
@ stdcall WaitForSingleObject() kernel32.WaitForSingleObject
@ stdcall WaitForSingleObjectEx() kernel32.WaitForSingleObjectEx
@ stub WaitOnAddress
@ stdcall -version=0x600+ WakeAllConditionVariable() kernel32.WakeAllConditionVariable
@ stub WakeByAddressAll
@ stub WakeByAddressSingle
@ stdcall -version=0x600+ WakeConditionVariable() kernel32.WakeConditionVariable